from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('upload-photo/', views.upload_photo, name='upload_photo'),
    path('photos/', views.user_photos, name='user_photos'),
]
