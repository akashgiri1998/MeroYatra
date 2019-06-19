from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('Signup/',views.SignUp,name='Signup'),
    path('addUser/',views.addUser,name='addUser'),
    path('login/', auth_views.LoginView.as_view(template_name = 'Yatri/home.html'), name= 'log_in'),
]