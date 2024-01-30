from django.urls import path
from .views import *

app_name='figure'

urlpatterns = [
    path('/', figure, name='main'),
]