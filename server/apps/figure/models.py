from django.db import models

class Figure(models.Model):
    name = models.CharField(max_length=20)
    image_path = models.CharField(max_length = 255)