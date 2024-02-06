from django.db import models

# Create your models here.
class GameRoom(models.Model):
    room_name = models.CharField(max_length=32)

    order_game = models.CharField(max_length=50)
    ran_figure = models.CharField(max_length=50, null = True, blank = True)
    ran_four = models.CharField(max_length=50, null = True, blank = True)
    ran_movie = models.CharField(max_length=50, null = True, blank = True)
    ran_music = models.CharField(max_length=50, null = True, blank = True)
    
    
# class RandomMusic(models.Model):
#     room_id=models.ForeignKey(GameRoom, on_delete=models.CASCADE, verbose_name="Random_Music")
#     random_id=models.IntegerField()

# class RandomFour(models.Model):
#     room_id=models.ForeignKey(GameRoom, on_delete=models.CASCADE, verbose_name="Random_Four")
#     random_id=models.IntegerField()

# class RandomFigure(models.Model):
#     room_id=models.ForeignKey(GameRoom, on_delete=models.CASCADE, verbose_name="Random_Figure")
#     random_id=models.IntegerField()

# class RandomMovie(models.Model):
#     room_id=models.ForeignKey(GameRoom, on_delete=models.CASCADE, verbose_name="Random_Movie")
#     random_id=models.IntegerField()
