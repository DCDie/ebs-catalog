from django.contrib.auth.models import AbstractUser
from django.db import models

__all__ = [
    'CustomUser'
]


class CustomUser(AbstractUser):
    email = models.EmailField(
        'email address',
        blank=False,
        unique=True
    )

    REQUIRED_FIELDS = []
    USERNAME_FIELDS = 'email'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        app_label = 'users'
