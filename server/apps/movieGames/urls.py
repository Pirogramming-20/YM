from django.urls import path,include
from .views import *

app_name = 'movieGames'

urlpatterns = [
    path('/<int:roomId>/movie-game', movie_game_main, name='movie_game_main'),
    path('/<int:roomId>/movie-game/start/<int:count>', movie_game_start, name='movie_game_start'),
    path('/movie-game/next', next_quiz, name='next_quiz'),
    path('/movie-game/answer', answer, name='answer'),
]

