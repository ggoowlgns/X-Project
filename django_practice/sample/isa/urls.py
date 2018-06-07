from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("members/signup", views.signup),
    path("members/login", views.login),
    path("members/encode", views.str_encodedfile),
    path("photo/upload", views.upload_file),
]
