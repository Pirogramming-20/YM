from django.db import models

# Create your models here.

class ChatGame(models.Model):
    chatText = models.CharField(max_length=50)