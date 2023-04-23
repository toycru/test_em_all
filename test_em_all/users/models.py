from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    about_info = models.TextField(
    'О себе',
    blank=True,
    )

