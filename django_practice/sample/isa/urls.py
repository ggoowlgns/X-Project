from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("members/signup", views.signup),
    path("members/login", views.login),
    path("members/encode", views.str_encodedfile),
    path("face/get", views.give_encodingdata),
    path("photo/upload", views.upload_file),
    path("student/attend" ,views.stu_attend),

    path("subject/create" , views.sub_create),
    path("subject/get_subname" , views.sub_get),
    path("subject/get_subdetail" , views.sub_detail),
]
