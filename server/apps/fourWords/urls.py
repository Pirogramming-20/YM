from django.urls import path
from .views import *

app_name='fourWords'

urlpatterns = [
    path('', fourWords_main, name='fourWords_main'),
    path('fourWords_game/', fourWords_game_start, name='fourWords_game'),
    path('next_fourWords_ajax/', next_fourWords_ajax, name='fourWords_ajax'),
]
