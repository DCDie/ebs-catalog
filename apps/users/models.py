from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

__all__ = ["CustomUser", "CustomUserManager"]


class CustomUserManager(BaseUserManager):
    def create_user(
        self, email=None, password=None, is_staff=False, is_superuser=False
    ):
        if not email:
            raise ValueError("User must contain email")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email, password=password, is_staff=True, is_superuser=True
        )
        user.save()
        return user


class CustomUser(AbstractUser):
    email = models.EmailField("email address", blank=False, unique=True)
    username = None

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        app_label = "users"
        ordering = ["id"]
