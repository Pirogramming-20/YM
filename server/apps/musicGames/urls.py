from django.urls import path,include
from .views import *

app_name = 'musicGames'

urlpatterns = [
    path('/<int:roomId>/', music_game_main, name='music_game_main'),
    path('/<int:roomId>/music_game_2000/<int:count>', music_game_start_2000, name='music_game_start_2000'),
    path('/<int:roomId>/music_game_2010/<int:count>', music_game_start_2010, name='music_game_start_2010'),
    path('/<int:roomId>/music_game_2020/<int:count>', music_game_start_2020, name='music_game_start_2020'),
    path('/next/', next_quiz, name='next_quiz'),
    path('/answer/', answer, name='answer'),
]