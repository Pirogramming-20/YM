from django.db import models

# Create your models here.
class GameRoom(models.Model):
    room_name = models.CharField(max_length=32)

    order_game = models.CharField(max_length=50)
    ran_figure = models.CharField(max_length=50, null = True, blank = True)#,로 구분된 문자열
    ran_four = models.CharField(max_length=50, null = True, blank = True)
    ran_movie = models.CharField(max_length=50, null = True, blank = True)
    ran_music = models.CharField(max_length=50, null = True, blank = True)