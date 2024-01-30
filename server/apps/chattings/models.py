from django.db import models

# Create your models here.
class GameRoom(models.Model):
  room_name = models.CharField(max_length=32)