from django.urls import path
from .views import *

app_name='lookInside'

urlpatterns = [
    path('<int:roomId>', lookInside_main, name='lookInside_main'),
    path('<int:roomId>/lookInside_game/<int:count>', lookInside_game_start, name='lookInside_game'),
    path('next/', next_lookInside_ajax, name='lookInside_ajax'),
    path('answer/', answer, name='answer'),
    path('before/', before_lookInside_ajax, name='lookInside_ajax_before'),
]