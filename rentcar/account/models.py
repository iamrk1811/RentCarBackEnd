from django.db import models
from django.contrib.auth.models import  AbstractBaseUser
from django.contrib.auth.models import UserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]