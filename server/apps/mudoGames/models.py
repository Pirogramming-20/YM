from django.db import models

class Mudo(models.Model):
    line = models.CharField(max_length=100)
    image_path = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.answer
