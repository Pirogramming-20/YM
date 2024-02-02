from django.db import models
from django.conf import settings

# Create your models here.
class GameRoom(models.Model):
  room_name = models.CharField(max_length=32)
  created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='game_rooms', null=True, blank=True)