from django.urls import path
from .views import *

app_name='figure'

urlpatterns = [
    path('', figure_quiz, name='figure_quiz'),
    path('next_figure_ajax/', next_figure_ajax, name='figure_ajax'),
]