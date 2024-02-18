from django.db import models

# Create your models here.
class MusicGame_2000(models.Model):
    title = models.CharField('노래제목', max_length=30)
    music = models.TextField('노래 파일 경로')
    singer = models.CharField('가수', max_length=20)
    youtube = models.TextField('유튜브')

    def __str__(self):
        return self.title
    

class MusicGame_2010(models.Model):
    title = models.CharField('노래제목', max_length=30)
    music = models.TextField('노래 파일 경로')
    singer = models.CharField('가수', max_length=20)
    youtube = models.TextField('유튜브')

    def __str__(self):
        return self.title
    

class MusicGame_2020(models.Model):
    title = models.CharField('노래제목', max_length=30)
    music = models.TextField('노래 파일 경로')
    singer = models.CharField('가수', max_length=20)
    youtube = models.TextField('유튜브')

    def __str__(self):
        return self.title