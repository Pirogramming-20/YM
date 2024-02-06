from django.urls import path,include
from .views import *

app_name = 'movieGames'

urlpatterns = [
    path('movie-game', movie_game_main, name='movie_game_main'),
    path('movie-game/start', movie_game_start, name='movie_game_start'),
    path('movie-game/next', next_quiz, name='next_quiz'),
]

