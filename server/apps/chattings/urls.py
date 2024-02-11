from django.urls import path
from .views import *

app_name='rooms'

urlpatterns = [
    path('',main,name = 'main'),
    path('/create',create,name='create'),
    path('/detail/<int:pk>',detail,name='detail'),
    path('/detail-mobile/<int:pk>',detailMobile,name='detailMobile'),
    path('/next_game/<int:roomId>',next_game, name='next_game'),
    path('/finish/<int:roomId>',finish,name='finish'),
    path('/recreate/<int:roomId>',recreate,name='recreate'),
    path('/delete/<int:roomId>',delete,name='delete'),
    path('/re_game/<int:roomId>',re_game,name='re_game'),
]