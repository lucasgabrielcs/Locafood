from rest_framework import generics, permissions
from .serializers import RegisterSerializer
from .models import CustomUser

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class registro(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)
    authentication_classes = [] 