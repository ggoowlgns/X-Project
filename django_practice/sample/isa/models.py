from django.db import models
import  datetime
import os
# Create your models here.

class Members(models.Model):
    id = models.CharField(max_length=30,primary_key=True)
    name = models.CharField(max_length=30,default='pjh')
    passwd = models.CharField(max_length=30,default='0000')
    phone_num = models.IntegerField(default=0000)
    job =models.CharField(max_length=20 ,default='학생')
    pic_encode = models.TextField(default='0', null='0')
    imagefile = models.FileField(
        upload_to="data_analysis/uploadfile",
        default="NO_PIC",
        null='1',
    )
    attend = models.CharField(max_length=30 , default="0",null="0")

    def __str__(self):
        return self.name


class Subjects(models.Model):
    id_num = models.TextField(default="none",null="none")
    sub_name = models.CharField(max_length=50, default='none', null='none')
    pro_name = models.CharField(max_length=50 , default='none',null='none')

    def __str__(self):
        return self.sub_name
