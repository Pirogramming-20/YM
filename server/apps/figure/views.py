from django.shortcuts import render, redirect
from apps.chattings.models import GameRoom
from .models import Figure
import random
import json
from django.http import JsonResponse


#0. create figure db
#1. figure_game main page
def figure_main(request, roomId): #60개
    if roomId == 0:
        ctx = {
        'roomId' : roomId,
        }
        if request.method == "POST":
            count = int(request.POST['count'])
            ctx = {
            'roomId' : roomId,
            'count':count
            }
            return redirect('/figure/{0}/figure_game/{1}'.format(roomId,count))
        return render(request, "games/figure_main.html",ctx)

    room = GameRoom.objects.get(id=roomId)
    ctx = {
        'roomId' : roomId,
        'room':room
    }
    if request.method == "POST":
        count = int(request.POST['count'])
        ctx = {
        'roomId' : roomId,
        'room':room,
        'count':count
        }
        return redirect('/figure/{0}/figure_game/{1}'.format(roomId,count))
    return render(request, "games/figure_main.html",ctx)

def figure_game_start(request,roomId,count):
    #채팅룸 랜덤 아이디랑 연결
    if roomId == 0:
        quiz_id_int_list = random.sample(range(1,61),count)
    else:
        room = GameRoom.objects.get(id=roomId)
        quiz_id_list = room.ran_figure
        quiz_id_str_list = list(map(int, quiz_id_list.split(",")))
        quiz_id_int_list = quiz_id_str_list[:count]

    figure_game = [(quiz_id_int_list[0])]
    for quiz_id in quiz_id_int_list[1:]:
        figure_game.append(quiz_id)

    quiz_id = figure_game.pop(0)
    figure_game.append(quiz_id)
    quiz_figure = Figure.objects.get(id = quiz_id)

    if roomId == 0:
        ctx={
        'quiz_figure':quiz_figure,
        'count' : count,
        'roomId' : roomId,
        'figure_game' : figure_game,
        'quiz_id':quiz_id
        }
        return render(request, "games/figure_start.html", ctx)
    
    ctx={
        'quiz_figure':quiz_figure,
        'count' : count,
        'roomId' : roomId,
        'room':room,
        'figure_game' : figure_game,
        'quiz_id':quiz_id
    }
    
    return render(request, "games/figure_start.html", ctx)

def next_figure_ajax(request):
    req = json.loads(request.body)
    quiz_id = (req['id'])
    game_list=(req['game_list'])
    quiz_id = game_list.pop(0)
    game_list.append(quiz_id)

    figure = Figure.objects.get(id=quiz_id)
    image_path = figure.image_path

    return JsonResponse({'id':quiz_id, 'image_path': image_path, 'game_list':game_list})

def before_figure_ajax(request):
    req = json.loads(request.body)
    quiz_id = (req['id'])
    game_list=(req['game_list'])
  
    next_quiz_id = game_list.pop()
    game_list.insert(0,next_quiz_id)
    quiz_id = game_list[-1]

    figure = Figure.objects.get(id=quiz_id)
    image_path = figure.image_path

    return JsonResponse({'id':quiz_id, 'image_path': image_path, 'game_list':game_list})


def answer(request):
    req = json.loads(request.body)
    quiz_id = (req['id'])

    quiz = Figure.objects.get(id=quiz_id)
    name = quiz.name
    
    return JsonResponse({'id' : quiz_id, 'name' : name})