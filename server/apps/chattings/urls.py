from django.urls import path
from .views import *

app_name='rooms'

urlpatterns = [
    path('',main,name = 'main'),
    path('/create',create,name='create'),
    path('/chatroom/<int:pk>',chatroom,name='chatroom'),
    path('/choose/<int:pk>',choose,name='choose'),
]