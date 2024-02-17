from django.db import models

# Create your models here.
class LookInside(models.Model):
  name = models.CharField(max_length=20)
  image_path = models.CharField(max_length = 255, null=True)