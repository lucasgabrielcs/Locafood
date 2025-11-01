# accounts/urls.py
from django.urls import path
from .views import registro 
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView, 
)

urlpatterns = [
    path('register/', registro.as_view(), name='auth_register'),
    path('login/', TokenObtainPairView.as_view(), name='auth_login'),
    path('refresh/', TokenRefreshView.as_view(), name='auth_refresh'),
]