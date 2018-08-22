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

    path("student/check_stu",views.stu_detail),

    #라즈베리파이에서 들어옴
    path("student/attend" ,views.stu_attend),
    path("student/out", views.stu_out),
    #
    path("subject/create" , views.sub_create),
    path("subject/get_subname" , views.sub_get),
    path("subject/get_subdetail" , views.sub_detail),

    #V-ICE-R 송신기(Android) _test
    path("vicer/accel_on" , views.accel_on),
    path('vicer/accel_off', views.accel_off),


    #V-ICE-R 수신기(Arduino) _test
    #상태 계속 수신#
    path("vicer/status" , views.status_response),


]
