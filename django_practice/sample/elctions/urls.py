from django.contrib import admin
from django.urls import path
from django.conf.urls import *
from . import views

urlpatterns = [
    path("", views.index),
    path("areas/<str:area>/", views.areas)
]
