from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from .models import Members
from django.views.decorators.csrf import csrf_exempt
import MySQLdb
from django.template import RequestContext

from .forms import ImageForm
from django.urls import reverse
import json

import face_recognition
import cv2
import numpy as np
from PIL import Image

# Create your views here.

############db연결###########
# aws_ip =  "18.179.74.220"
aws_ip = "127.0.0.1"



def index(request):
    members = Members.objects.all() #해당 table의 모든 정보를 가져옴
    # no1 = Members.objects.filter(party_number = 1) #select party_number 한것만 가져옴
    str = ''
    for member in members:
        str += "id: {} <br> name: {} <br> passwd : {} <br> phone_num : {}".format(member.id,member.name,member.passwd, member.phone_num)


    #############context만들어서 html로 보내기########
    context = {'members': members}


    return render(request, 'isa/index.html',context)

@csrf_exempt
def signup(request):
    connection = MySQLdb.connect(host=aws_ip,
                                 user="root",
                                 passwd="root",
                                 db="xproj",
                                 use_unicode=True,
                                 charset="utf8")
    cursor = connection.cursor()

    if request.method == 'POST':
        id= request.POST.get('id')
        passwd = request.POST.get('passwd')
        name = request.POST.get('name')
        phone_num = request.POST.get('phone_num')
        job = request.POST.get('job')
	
        staff_data = [(str(id), str(passwd), str(name), str(phone_num),str(job))]
        for p in staff_data:
            format_str = """INSERT INTO isa_members (id , passwd , name , phone_num,job,attend, imagefile,pic_encode)
            VALUES ( '{id}' , '{passwd}', '{name}' , '{phone_num}','{job}','0','0','0');
            """

            sql_command = format_str.format(id=p[0], passwd=p[1], name=p[2], phone_num=p[3],job=p[4])
            print("inserted")
            cursor.execute(sql_command)

        #####conection 모두 종료########
        connection.commit()
        cursor.close()
        connection.close()

        print(id,passwd, name,phone_num)
        # return render(request,'isa/index.html', context)

    return HttpResponse()


@csrf_exempt
def login(request):
    connection = MySQLdb.connect(host=aws_ip,
                                 user="root",
                                 passwd="root",
                                 db="xproj",
                                 use_unicode=True,
                                 charset="utf8")
    cursor = connection.cursor()

    if request.method == 'POST':
        id= request.POST.get('id')
        passwd = request.POST.get('passwd')

        staff_data = [(str(id), str(passwd))]
        for p in staff_data:
            print(p[0])
            format_str = """SELECT passwd,job,name FROM isa_members WHERE id={id};
            """

            sql_command = format_str.format(id=p[0])
            login_boolean=cursor.execute(sql_command) #0 : 아이디 없을때 1 : 아이디 존재
            fetall=cursor.fetchall()
            print('login_boolean : ',login_boolean)

            if login_boolean == 1:
                if fetall[0][0] == passwd:
                    print('입력받은 password', fetall[0][0])
                    return HttpResponse(fetall[0][1]+"/"+fetall[0][2])

        #####conection 모두 종료########
        connection.commit()
        cursor.close()
        connection.close()


    return HttpResponse()

import time
@csrf_exempt
def upload_file(request):
    connection = MySQLdb.connect(host=aws_ip,
                                 user="root",
                                 passwd="root",
                                 db="xproj",
                                 use_unicode=True,
                                 charset="utf8")
    cursor = connection.cursor()

    if request.method == 'POST':
        form = ImageForm(request.POST , request.FILES)
        if form.is_valid():
            newimg = Members(imagefile = request.FILES['imagefile'])
            newimg.save()
            time.sleep(1)

            temp_path = '/home/ubuntu/git/X-Project/django_practice/sample/media/data_analysis/uploadfile/'+str(request.FILES['imagefile'])
            print(temp_path)
            temp_img = face_recognition.load_image_file(temp_path)
            temp_encoding = face_recognition.face_encodings(temp_img)
            print(temp_encoding[0])
            
            staff_data = [[str(request.FILES['imagefile']).split(".")[0], str(temp_encoding[0])]]
            for p in staff_data:
                format_str = "UPDATE isa_members set pic_encode=\'"+p[1]+"\' WHERE id =\'"+p[0]+"\';"
                print(format_str)

                sql_command = format_str
                cursor.execute(sql_command)

            print("added pic_encode")

        #####conection 모두 종료########
        connection.commit()
        cursor.close()
        connection.close()
    return HttpResponse("pic_encode added")


            
@csrf_exempt
def str_encodedfile(request):
    connection = MySQLdb.connect(host=aws_ip,
                                 user="root",
                                 passwd="root",
                                 db="xproj",
                                 use_unicode=True,
                                 charset="utf8")
    cursor = connection.cursor()

    if request.method == 'POST':
        staff_data = [(str(id), str(pic_encode))]
        for p in staff_data:
            format_str = "UPDATE isa_members set pic_encode='"+pic_encode+"' WHERE id = '"+id+"';"
            print(format_str)

            sql_command = format_str
            cursor.execute(sql_command)

            print("added pic_encode")

        #####conection 모두 종료########
        connection.commit()
        cursor.close()
        connection.close()
    return HttpResponse("pic_encode added")

@csrf_exempt
def give_encodingdata(request):
    connection = MySQLdb.connect(host=aws_ip,
                                 user="root",
                                 passwd="root",
                                 db="xproj",
                                 use_unicode=True,
                                 charset="utf8")
    cursor = connection.cursor()
    format_str = """SELECT id,pic_encode FROM isa_members;
                """

    sql_command = format_str
    login_boolean = cursor.execute(sql_command)  # 0 : 아이디 없을때 1 : 아이디 존재
    fetall = cursor.fetchall()
    return HttpResponse(fetall)


@csrf_exempt
def stu_attend(request):
    connection = MySQLdb.connect(host=aws_ip,
                                 user="root",
                                 passwd="root",
                                 db="xproj",
                                 use_unicode=True,
                                 charset="utf8")
    cursor = connection.cursor()

    if request.method == 'POST':
        id = request.POST.get('id')
        format_str = "UPDATE isa_members set attend= \'" + str(1) + "\' WHERE id = \'" + id + "\';"
        print(format_str)

        sql_command = format_str
        cursor.execute(sql_command)
    #####conection 모두 종료########
    connection.commit()
    cursor.close()
    connection.close()

    return HttpResponse("attend changed")


@csrf_exempt
def sub_create(request):
    connection = MySQLdb.connect(host=aws_ip,
                                 user="root",
                                 passwd="root",
                                 db="xproj",
                                 use_unicode=True,
                                 charset="utf8")
    cursor = connection.cursor()

    if request.method == 'POST':
        id_num = request.POST.get('id_num')
        sub_name = request.POST.get('sub_name')
        pro_name = request.POST.get('pro_name')

        staff_data = [(str(id_num), str(sub_name), str(pro_name))]
        for p in staff_data:
            format_str = """INSERT INTO isa_subjects (id_num , sub_name , pro_name)
            VALUES ( '{id_num}' , '{sub_name}', '{pro_name}' );
            """

            sql_command = format_str.format(id_num=p[0], sub_name=p[1], pro_name=p[2])
            print("inserted")
            cursor.execute(sql_command)

        #####conection 모두 종료########
        connection.commit()
        cursor.close()
        connection.close()


    return HttpResponse()


@csrf_exempt
def sub_get(request):
    connection = MySQLdb.connect(host=aws_ip,
                                 user="root",
                                 passwd="root",
                                 db="xproj",
                                 use_unicode=True,
                                 charset="utf8")
    cursor = connection.cursor()
    sub_names = ""
    if request.method == 'POST':
        pro_name= request.POST.get('pro_name')


        format_str = "SELECT sub_name FROM isa_subjects WHERE pro_name=\'"+pro_name+"\';"
        login_boolean=cursor.execute(format_str) #0 : 아이디 없을때 1 : 아이디 존재
        fetall=cursor.fetchall()
        print('login_boolean : ',login_boolean)
        print(fetall)
        print(len(fetall))
        if login_boolean != 0:
            for i in range(0,len(fetall)):
                sub_names += (fetall[i][0]+"/")
        else:
            return HttpResponse(600)
        return HttpResponse(sub_names)
        #####conection 모두 종료########
        connection.commit()
        cursor.close()
        connection.close()

    return HttpResponse("error")


@csrf_exempt
def sub_detail(request):
    connection = MySQLdb.connect(host=aws_ip,
                                 user="root",
                                 passwd="root",
                                 db="xproj",
                                 use_unicode=True,
                                 charset="utf8")
    cursor = connection.cursor()

    if request.method == 'POST':
        sub_name = request.POST.get('sub_name')
        format_str = "SELECT id_num FROM isa_subjects WHERE sub_name=\'" + sub_name+ "\';"

        login_boolean = cursor.execute(format_str)  # 0 : 아이디 없을때 1 : 아이디 존재
        fetall = cursor.fetchall()
        print('login_boolean : ', login_boolean)
        
        stu_names = fetall[0][0]
        
        send = ""
        print(stu_names.split("/")[:-1])
        for stu_name in stu_names.split("/")[:-1]:
            print("stuname:   "+stu_name)
            format_str2 = "SELECT attend FROM isa_members WHERE id=\'" + stu_name + "\';"
            login_boolean = cursor.execute(format_str2)  # 0 : 아이디 없을때 1 : 아이디 존재
            fetall2 = cursor.fetchall()
            print(fetall2)
            send += (stu_name+":"+fetall2[0][0]+"/")
        #####conection 모두 종료########
        connection.commit() 
        cursor.close()
        connection.close()
        return HttpResponse(send)
    
    return HttpResponse("error")

