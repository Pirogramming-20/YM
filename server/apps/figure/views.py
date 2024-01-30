from django.shortcuts import render
from .models import Figure
import random

def ran_Id():
    return random.sample(range(1,6), 5)
# id_list = ran_Id() #랜덤 아이디 리스트
def get_image_list(id_list):
    figures_list = []
    for i in range(5):
        figure = Figure.objects.get(id=id_list[i])
        figures_list.append(figure)
    return figures_list

def figure(request):
    id_list = ran_Id()
    figures_list = get_image_list(id_list)
    figure = figures_list[0]
    ctx={
        'figure' : figure,
    }
    
    return render(request, 'games/figure.html', ctx)

