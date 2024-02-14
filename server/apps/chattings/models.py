from django.db import models
from django.conf import settings

from apps.main.models import User

# Create your models here.
class GameRoom(models.Model):
    room_name = models.CharField(max_length=32, unique=True)

    order_game = models.CharField(max_length=50)
    order_num = models.CharField(max_length=10, null = True, blank = True)
    ran_figure = models.CharField(max_length=50, null = True, blank = True)#,로 구분된 문자열
    ran_four = models.CharField(max_length=50, null = True, blank = True)
    ran_movie = models.CharField(max_length=50, null = True, blank = True)
    ran_music = models.CharField(max_length=50, null = True, blank = True)
    ran_look = models.CharField(max_length=50, null = True, blank = True)
    ran_chat = models.CharField(max_length=50, null = True, blank = True)

    participants = models.IntegerField(default = 0)
    
    user_id=models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")