from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

