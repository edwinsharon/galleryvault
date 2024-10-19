from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    
]

urlpatterns = [
    path('photos/', views.user_gallery, name='user-gallery'),
    path('photos/<int:pk>/', views.photo_detail, name='photo-detail'),
    path('photos/token/', views.get_token, name='get-token'),
    path('photos/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('photos/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
