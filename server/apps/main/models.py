from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # room_count = models.IntegerField(default = 0)

    def __str__(self):
        return self.username