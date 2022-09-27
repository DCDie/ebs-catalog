from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

User = get_user_model()


class UserTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='simple@test.com',
            first_name='simple_first_name',
            last_name='simple_last_name',
            username='simple@test.com',
            is_superuser=False,
            is_staff=False,
        )
        self.user_password = 'simple'
        self.user.set_password(self.user_password)
        self.user.save()
        self.user_refresh = RefreshToken.for_user(self.user)

    # User get access token
    def test_user_login(self):
        data = {
            'username': self.user.email,
            'password': self.user_password
        }
        response = self.client.post(
            path='/users/login',
            data=data,
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_user_register(self):
        data = {
            'email': 'test@email.com',
            'password': self.user_password
        }
        response = self.client.post(
            path='/users/register',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_user_refresh_token(self):
        data = {
            "refresh": str(self.user_refresh)
        }
        response = self.client.post(
            '/token/refresh',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_user_list(self):
        response = self.client.get(
            '/users'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
