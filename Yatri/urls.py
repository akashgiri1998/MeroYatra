from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Signup/',views.SignUp,name='Signup'),
    path('addUser/',views.addUser,name='addUser'),
]