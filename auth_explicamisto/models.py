from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    telephone = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=50, blank=True)


    

