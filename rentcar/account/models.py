from django.db import models
from django.contrib.auth.models import  AbstractBaseUser
from datetime import datetime
from account.managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    is_staff = models.BooleanField(
        ('staff status'),
        default=False,
        help_text=('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        ('active'),
        default=False,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_superuser =  models.BooleanField(
        ('Super User'),
        default=False
    )
    date_joined = models.DateTimeField(('date joined'), default=datetime.now())
    # Details of the user
    email = models.EmailField(('email address'), max_length=255, unique=True, null=True)
    mobile = models.CharField(
        ('mobile number'), max_length=12, blank=True, null=True, db_index=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def has_perm(self, perm, obj=None):
       return self.is_staff

    def has_module_perms(self, app_label):
       return self.is_staff


# class UserProfile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)