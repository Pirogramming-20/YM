from django.urls import path
from .views import *

app_name='fourWords'

urlpatterns = [
    path('<int:roomId>', fourWords_main, name='fourWords_main'),
    path('<int:roomId>/fourWords_game/<int:count>', fourWords_game_start, name='fourWords_game'),
    path('next/', next_fourWords_ajax, name='fourWords_ajax'),
    path('answer/', answer, name='answer'),
    path('before/', before_fourWords_ajax, name='fourWords_ajax_before'),
]
