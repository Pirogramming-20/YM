from django.db import models

class Four(models.Model):
    two = models.CharField(max_length=20, null=True, blank=True)
    answer = models.CharField(max_length=20)

    def two_save(self):
        if self.answer and not self.two:
            self.two = self.answer[:2]
            super().save()        

class QuizFour(models.Model):
    four_quiz_id = models.ForeignKey(Four, on_delete=models.CASCADE)