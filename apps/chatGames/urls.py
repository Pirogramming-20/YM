from django.urls import path
from .views import *

app_name='chatGames'

urlpatterns = [
    path('<int:roomId>', chatGames_main, name='chatGames_main'),
    path('<int:roomId>/chatGames_game/<int:count>', chatGames_game_start, name='chatGames_game'),
    path('next/', next_chatGames_ajax, name='chatGames_ajax'),
    # path('answer/', answer, name='answer'),
    path('before/', before_chatGames_ajax, name='chatGames_ajax_before'),
]