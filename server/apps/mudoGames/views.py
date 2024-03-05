from django.shortcuts import render, redirect
from apps.chattings.models import GameRoom
from .models import Mudo
import random
import json
from django.http import JsonResponse

def mudo_main(request, roomId):#50개
    
    if roomId == 0:
        ctx = {
            'roomId' : roomId,
        }
        if request.method == "POST":
            count = int(request.POST['count'])
            ctx = {
                'roomId' : roomId,
                'count' : count
            }
            return redirect('/mudo/{0}/mudo_game/{1}'.format(roomId,count))
        return render(request, "mudoGames/mudo_main.html", ctx)
    
    room = GameRoom.objects.get(id=roomId)
    ctx = {
        'roomId' : roomId,
        'room' : room
    }
    if request.method == "POST":
        count = int(request.POST['count'])
        ctx = {
            'roomId' : roomId,
            'room' : room,
            'count' : count
        }
        return redirect('/mudo/{0}/mudo_game/{1}'.format(roomId,count))
    return render(request, "mudoGames/mudo_main.html", ctx)

def mudo_game_start(request, roomId, count):
    if roomId == 0:
        quiz_id_int_list = random.sample(range(1,51),count) #최대 20개
    else:
        room = GameRoom.objects.get(id=roomId)
        quiz_id_list = room.ran_mudo
        quiz_id_str_list = list(map(int, quiz_id_list.split(",")))
        quiz_id_int_list = quiz_id_str_list[:count]

    mudo_game = [(quiz_id_int_list[0])]
    for quiz_id in quiz_id_int_list[1:]:
        mudo_game.append(quiz_id)

    quiz_id = mudo_game.pop(0)
    mudo_game.append(quiz_id)
    quiz_mudo = Mudo.objects.get(id = quiz_id)

    if roomId == 0:
        ctx={
            'quiz_mudo' : quiz_mudo,
            'count' : count,
            'roomId' : roomId,
            'mudo_game' : mudo_game,
            'quiz_id':quiz_id
        }
        return render(request, "mudoGames/mudo_start.html", ctx)
    
    ctx = {
        'quiz_mudo' : quiz_mudo,
        'count' : count,
        'roomId' : roomId,
        'room' : room,
        'mudo_game' : mudo_game,
    }
    return render(request, "mudoGames/mudo_start.html", ctx)

def next_mudo_ajax(request):
    req = json.loads(request.body)
    quiz_id = (req['id'])
    game_list=(req['game_list'])
    quiz_id = game_list.pop(0)
    game_list.append(quiz_id)

    mudo = Mudo.objects.get(id=quiz_id)
    image_path = mudo.image_path

    return JsonResponse({'id':quiz_id, 'image_path': image_path, 'game_list':game_list})

def before_mudo_ajax(request):
    req = json.loads(request.body)
    quiz_id = (req['id'])
    game_list=(req['game_list'])
  
    next_quiz_id = game_list.pop()
    game_list.insert(0,next_quiz_id)
    quiz_id = game_list[-1]

    mudo = Mudo.objects.get(id=quiz_id)
    image_path = mudo.image_path

    return JsonResponse({'id':quiz_id, 'image_path': image_path, 'game_list':game_list})

def answer(request):
    req = json.loads(request.body)
    quiz_id = (req['id'])

    quiz = Mudo.objects.get(id=quiz_id)
    line = quiz.line
    
    return JsonResponse({'id' : quiz_id, 'line' : line})