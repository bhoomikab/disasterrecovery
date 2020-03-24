from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib.auth.decorators import login_required


# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_contractor = models.BooleanField(default=False)


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'user'


class Contractor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'user'
