from django.urls import path
from .views import *

app_name='bodyGames'

urlpatterns = [
    path('/<int:roomId>/', body_game_main, name='body_game_main'),
    path('/<int:roomId>/body_game_animal/<int:count>', body_game_start_animal, name='body_game_start_animal'),
    path('/<int:roomId>/body_game_food/<int:count>', body_game_start_food, name='body_game_start_food'),
    path('/<int:roomId>/body_game_thing/<int:count>', body_game_start_thing, name='body_game_start_thing'),
    path('/<int:roomId>/body_game_job/<int:count>', body_game_start_job, name='body_game_start_job'),
    path('/<int:roomId>/body_game_proverb/<int:count>', body_game_start_proverb, name='body_game_start_proverb'),
    path('/next/', next_quiz, name='next_quiz'),
    path('/before/', before_quiz, name='before_quiz'),
]