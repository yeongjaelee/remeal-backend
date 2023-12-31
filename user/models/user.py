import secrets

from django.contrib.auth.models import AbstractUser
from django.db import models

from user.managers.user_manager import UserManager


# Create your models here.


class User(AbstractUser):
    objects = UserManager()
    token = models.CharField(max_length=255, null=True)
    refresh_token = models.CharField(max_length=255, null=True)

    def __str__(self):
        return '{}'.format(self.email)
    def generate_verification_token(self):
        """
        Generates a random verification token for the user.
        """
        token = secrets.token_hex(16)
        self.verification_token = token
        self.save()
        return token

    class Meta:
        db_table = 'user'
