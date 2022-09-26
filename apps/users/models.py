from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import gettext_lazy as _

__all__ = [
    'CustomUser'
]


class CustomUser(AbstractUser):

    username = models.EmailField(
        _('email address'),
        blank=False,
        unique=True
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        app_label = 'users'