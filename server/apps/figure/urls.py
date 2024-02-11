from django.urls import path
from .views import *

app_name='figure'

urlpatterns = [
    path('<int:roomId>', figure_main, name='figure_main'),
    path('<int:roomId>/figure_game/<int:count>', figure_game_start, name='figure_game'),
    path('next/', next_figure_ajax, name='figure_ajax'),
    path('answer/', answer, name='answer'),
    path('before/', before_figure_ajax, name='figure_ajax_before'),
]