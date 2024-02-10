from django.urls import path,include
from .views import *

app_name = 'movieGames'

urlpatterns = [
    path('/<int:roomId>/', movie_game_main, name='movie_game_main'),
    path('/<int:roomId>/movie_game/<int:count>', movie_game_start, name='movie_game_start'),
    path('/next/', next_quiz, name='next_quiz'),
    path('/answer/', answer, name='answer'),
]

