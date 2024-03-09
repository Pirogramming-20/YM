from django.db import models

# Create your models here.
class GameImage(models.Model):
  answer = models.CharField(max_length=32)
  my_file = models.FileField(upload_to='uploads/')