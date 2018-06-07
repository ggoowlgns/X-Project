from django.db import models
import  datetime
import os
# Create your models here.

class Members(models.Model):
    id = models.CharField(max_length=30,primary_key=True)
    name = models.CharField(max_length=30,null='pjh')
    passwd = models.CharField(max_length=30,null='0000')
    phone_num = models.IntegerField( default=1,null=0000)
    job =models.CharField(max_length=20 ,null='학생')
    pic_encode = models.TextField(null='0')

    def __str__(self):
        return self.name




class Image(models.Model):
    imagefile = models.FileField(
        upload_to="data_analysis/uploadfile"
    )

