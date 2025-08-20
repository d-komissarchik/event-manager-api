from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer


class UserRegisterViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


