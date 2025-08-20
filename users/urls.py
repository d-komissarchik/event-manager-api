from django.urls import path
from .views import UserRegisterViewSet


urlpatterns = [
    path('register/', UserRegisterViewSet.as_view(), name='user_register'),
]