from django.urls import path,include
from .views import *

app_name = 'musicGames'

urlpatterns = [
    path('music-game', music_game_main, name='music_game_main'),
    path('music-game/start-2000', music_game_start_2000, name='music_game_start_2000'),
    path('music-game/start-2010', music_game_start_2010, name='music_game_start_2010'),
    path('music-game/start-2020', music_game_start_2020, name='music_game_start_2020'),
    path('music-game/next', next_quiz, name='next_quiz'),
]