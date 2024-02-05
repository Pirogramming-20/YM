from django.db import models

# Create your models here.
class MovieGame(models.Model):
    title = models.CharField('영화제목', max_length=30)
    scene = models.TextField('명장면 사진 경로')
    line = models.TextField('명대사')

    def __str__(self):
        return self.title
    

class QuizList(models.Model):
	# Tony: 이 ForeignKey 관계는 MovieGame 1개에 QuizList 여러개인 관계인데,
	# Tony: 데이터 항목으로 보아할 때 자연스러운 관계 같지 않아보입니다.
    movie_game_id = models.ForeignKey(MovieGame, on_delete=models.CASCADE)