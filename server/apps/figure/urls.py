from django.urls import path
from .views import *

app_name='figure'

urlpatterns = [
    path('<int:roomId>', figure_main, name='figure_main'),
    path('<int:roomId>/figure_game/', figure_game_start, name='figure_game'),
    path('next_figure_ajax/', next_figure_ajax, name='figure_ajax'),
]