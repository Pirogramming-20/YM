from django.db import models

# Create your models here.
class MusicGame(models.Model):
    title = models.CharField('노래제목', max_length=30)
    music = models.TextField('노래 파일 경로')

    def __str__(self):
        return self.title
    

class QuizList(models.Model):
    music_game_id = models.ForeignKey(MusicGame, on_delete=models.CASCADE)