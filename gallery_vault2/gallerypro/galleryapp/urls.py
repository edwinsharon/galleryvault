from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name="index"),
    path('usersignin',views.usersignin,name="usersignin"),
    path('createuser',views.usersignup,name="createuser"),
    path('newpost',views.newpost,name="newpost"),
    path('logoutuser',views.logoutuser,name="logoutuser"),
    path('view_image/<int:pk>',views.view_image,name="view_image"),
    path('delete_image/<int:pk>',views.delete_image,name="delete_image"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
