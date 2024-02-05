from django.db import models

# Create your models here.
class GameRoom(models.Model):
    room_name = models.CharField(max_length=32)

    order_game = models.CharField(max_length=50)
    ran_figure = models.CharField(max_length=50, null = True, blank = True)
    ran_four = models.CharField(max_length=50, null = True, blank = True)
    ran_movie = models.CharField(max_length=50, null = True, blank = True)
    ran_music = models.CharField(max_length=50, null = True, blank = True)