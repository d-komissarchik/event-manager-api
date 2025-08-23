from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


class UserTests(APITestCase):
    def test_user_register_success(self):
        url = "/api/auth/register/"
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword123"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="testuser").exists())

    def test_user_register_duplicate(self):
        User.objects.create_user(username="testuser", email="test@example.com", password="123456")
        url = "/api/auth/register/"
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "anotherpass"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_obtain_token(self):
        user = User.objects.create_user(username="testuser", email="test@example.com", password="123456")
        url = "/api/auth/token/"
        data = {
            "username": "testuser",
            "password": "123456"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_token_refresh(self):
        user = User.objects.create_user(username="testuser", email="test@example.com", password="123456")
        refresh = RefreshToken.for_user(user)
        url = "/api/auth/token/refresh/"
        data = {"refresh": str(refresh)}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

