from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('usersignin',views.usersignin,name="usersignin"),
    path('createuser',views.usersignup,name="createuser"),
    path('newpost',views.newpost,name="newpost"),
    path('logoutuser',views.logoutuser,name="logoutuser")
]
