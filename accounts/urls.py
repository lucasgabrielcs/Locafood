# accounts/urls.py
from django.urls import path
from .views import registro # Importa a sua view 'registro'
from rest_framework_simplejwt.views import (
    TokenObtainPairView, # A view de login que já vem pronta
    TokenRefreshView,  # A view de refresh que já vem pronta
)

urlpatterns = [
    path('register/', registro.as_view(), name='auth_register'),
    path('login/', TokenObtainPairView.as_view(), name='auth_login'),
    path('refresh/', TokenRefreshView.as_view(), name='auth_refresh'),
]