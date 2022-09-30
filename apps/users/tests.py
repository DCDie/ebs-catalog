from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


def auth(user):
    refresh = RefreshToken.for_user(user)
    return {"HTTP_AUTHORIZATION": f"Bearer {refresh.access_token}"}


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email="simple@test.com",
            first_name="simple_first_name",
            last_name="simple_last_name",
            is_superuser=False,
            is_staff=False,
        )
        self.user_password = "simple"
        self.user.set_password(self.user_password)
        self.user.save()
        self.user_refresh = RefreshToken.for_user(self.user)

    # User get access token
    def test_user_login(self):
        data = {"email": self.user.email, "password": self.user_password}
        response = self.client.post(
            path="/users/login",
            data=data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_register(self):
        data = {"email": "test@email.com", "password": self.user_password}
        response = self.client.post(path="/users/register", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_refresh_token(self):
        data = {"refresh": str(self.user_refresh)}
        response = self.client.post("/token/refresh", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_list(self):
        response = self.client.get("/users", **auth(self.user))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
