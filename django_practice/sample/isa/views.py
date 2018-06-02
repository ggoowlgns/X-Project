from django.shortcuts import render
from django.http import HttpResponse
from .models import Members
from django.views.decorators.csrf import csrf_exempt
import MySQLdb
import json
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

        staff_data = [(str(id), str(passwd), str(name), str(phone_num))]
        for p in staff_data:
            format_str = """INSERT INTO isa_members (id , passwd , name , phone_num)
            VALUES ( '{id}' , '{passwd}', '{name}' , '{phone_num}');
            """

            sql_command = format_str.format(id=p[0], passwd=p[1], name=p[2], phone_num=p[3])
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
            format_str = """SELECT passwd FROM isa_members WHERE id={id};
            """

            sql_command = format_str.format(id=p[0])
            login_boolean=cursor.execute(sql_command) #0 : 아이디 없을때 1 : 아이디 존재
            fetall=cursor.fetchall()
            print('login_boolean : ',login_boolean)

            if login_boolean == 1:
                if fetall[0][0] == passwd:
                    print('입력받은 password', fetall[0][0])
                    return HttpResponse('1')

        #####conection 모두 종료########
        connection.commit()
        cursor.close()
        connection.close()


    return HttpResponse()