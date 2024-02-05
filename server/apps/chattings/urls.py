from django.urls import path
from .views import *

app_name='rooms'

urlpatterns = [
    path('',main,name = 'main'),
    path('create',create,name='create'),
    path('detail/<int:pk>',detail,name='detail'),
    path('next_game',next_game, name='next_game'),
]