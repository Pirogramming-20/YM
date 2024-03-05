from django.db import models

# Create your models here.
#주제 : 동물, 음식, 물건, 직업, 속담
class BodyGame_animal(models.Model):
    word = models.CharField(max_length=20)

class BodyGame_food(models.Model):
    word = models.CharField(max_length=20)

class BodyGame_thing(models.Model):
    word = models.CharField(max_length=20)

class BodyGame_job(models.Model):
    word = models.CharField(max_length=20)

class BodyGame_proverb(models.Model):
    word = models.TextField()