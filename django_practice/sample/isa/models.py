from django.db import models

# Create your models here.

class Members(models.Model):
    id = models.CharField(max_length=30,primary_key=True)
    name = models.CharField(max_length=30,null='pjh')
    passwd = models.CharField(max_length=30,null='0000')
    phone_num = models.IntegerField( default=1,null=0000)

    def __str__(self):
        return self.name