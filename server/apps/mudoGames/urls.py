from django.urls import path
from .views import *

app_name='mudoGames'

urlpatterns = [
    path('/<int:roomId>', mudo_main, name='mudo_main'),
    path('/<int:roomId>/mudo_game/<int:count>', mudo_game_start, name='mudo_game'),
    path('/next/', next_mudo_ajax, name='mudo_ajax'),
    path('/answer/', answer, name='answer'),
    path('/before/', before_mudo_ajax, name='mudo_ajax_before'),
]