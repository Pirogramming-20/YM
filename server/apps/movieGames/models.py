from django.db import models

# Create your models here.
class MovieGame(models.Model):
    title = models.CharField('영화제목', max_length=30)
    scene = models.TextField('명장면 사진 경로')
    line = models.TextField('명대사')

    def __str__(self):
        return self.title