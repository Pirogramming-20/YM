from django.shortcuts import render, redirect
from apps.chattings.models import GameRoom
from . models import *
import random
from django.http import JsonResponse
import json

# Create your views here.
def body_game_main(request, roomId):    
    room = GameRoom.objects.get(id=roomId)
    if request.method == 'POST':
        count = int(request.POST['count'])
        type = request.POST['type']
        ctx = {
            'roodId' : roomId,
            'room' : room,
            'count' : count,
        }

        if type == 'animal':
            return redirect('/body/{0}/body_game_animal/{1}'.format(roomId, count))
        elif type == 'food':
            return redirect('/body/{0}/body_game_food/{1}'.format(roomId, count))
        elif type == 'thing':
            return redirect('/body/{0}/body_game_thing/{1}'.format(roomId, count))
        elif type == 'job':
            return redirect('/body/{0}/body_game_job/{1}'.format(roomId, count))
        elif type == 'proverb':
            return redirect('/body/{0}/body_game_proverb/{1}'.format(roomId, count))
    
    ctx = {
        'roomId' : roomId,
        'room' : room,
    }
    return render(request, 'bodyGames/body_game_main.html', ctx)

def body_game_start_animal(request, roomId, count):
    room = GameRoom.objects.get(id=roomId)
    quiz_id_list = room.ran_body
    quiz_id_str_list = list(map(int, quiz_id_list.split(",")))
    quiz_id_int_list = quiz_id_str_list[:count]

    word = BodyGame_animal.objects.all()
    body_game = []
    print(quiz_id_int_list)
    print(word)
    for quiz_id in quiz_id_int_list:
        body_game.append(word[quiz_id-1].id)
    
    quiz_id = body_game.pop(0)
    body_game.append(quiz_id)
    quiz = BodyGame_animal.objects.get(id = quiz_id)

    ctx = {
        'quiz' : quiz,
        'roomId' : roomId,
        'room' : room,
        'count' : count,
        'body_game' : body_game,
        'type' : 'animal',
    }
    return render(request, 'bodyGames/body_game_start.html', ctx)

def body_game_start_food(request, roomId, count):
    room = GameRoom.objects.get(id=roomId)
    quiz_id_list = room.ran_body
    quiz_id_str_list = list(map(int, quiz_id_list.split(",")))
    quiz_id_int_list = quiz_id_str_list[:count]

    word = BodyGame_food.objects.all()
    body_game = []
    for quiz_id in quiz_id_int_list:
        body_game.append(word[quiz_id-1].id)
    
    quiz_id = body_game.pop(0)
    body_game.append(quiz_id)
    quiz = BodyGame_food.objects.get(id = quiz_id)

    ctx = {
        'quiz' : quiz,
        'roomId' : roomId,
        'room' : room,
        'count' : count,
        'body_game' : body_game,
        'type' : 'food',
    }
    return render(request, 'bodyGames/body_game_start.html', ctx)

def body_game_start_thing(request, roomId, count):
    room = GameRoom.objects.get(id=roomId)
    quiz_id_list = room.ran_body
    quiz_id_str_list = list(map(int, quiz_id_list.split(",")))
    quiz_id_int_list = quiz_id_str_list[:count]

    word = BodyGame_thing.objects.all()
    body_game = []
    for quiz_id in quiz_id_int_list:
        body_game.append(word[quiz_id-1].id)
    
    quiz_id = body_game.pop(0)
    body_game.append(quiz_id)
    quiz = BodyGame_thing.objects.get(id = quiz_id)

    ctx = {
        'quiz' : quiz,
        'roomId' : roomId,
        'room' : room,
        'count' : count,
        'body_game' : body_game,
        'type' : 'thing',
    }
    return render(request, 'bodyGames/body_game_start.html', ctx)

def body_game_start_job(request, roomId, count):
    room = GameRoom.objects.get(id=roomId)
    quiz_id_list = room.ran_body
    quiz_id_str_list = list(map(int, quiz_id_list.split(",")))
    quiz_id_int_list = quiz_id_str_list[:count]

    word = BodyGame_job.objects.all()
    body_game = []
    for quiz_id in quiz_id_int_list:
        body_game.append(word[quiz_id-1].id)
    
    quiz_id = body_game.pop(0)
    body_game.append(quiz_id)
    quiz = BodyGame_job.objects.get(id = quiz_id)

    ctx = {
        'quiz' : quiz,
        'roomId' : roomId,
        'room' : room,
        'count' : count,
        'body_game' : body_game,
        'type' : 'job',
    }
    return render(request, 'bodyGames/body_game_start.html', ctx)

def body_game_start_proverb(request, roomId, count):
    room = GameRoom.objects.get(id=roomId)
    quiz_id_list = room.ran_body
    quiz_id_str_list = list(map(int, quiz_id_list.split(",")))
    quiz_id_int_list = quiz_id_str_list[:count]

    word = BodyGame_proverb.objects.all()
    body_game = []
    for quiz_id in quiz_id_int_list:
        body_game.append(word[quiz_id-1].id)
    
    quiz_id = body_game.pop(0)
    body_game.append(quiz_id)
    quiz = BodyGame_proverb.objects.get(id = quiz_id)

    ctx = {
        'quiz' : quiz,
        'roomId' : roomId,
        'room' : room,
        'count' : count,
        'body_game' : body_game,
        'type' : 'proverb',
    }
    return render(request, 'bodyGames/body_game_start.html', ctx)

def next_quiz(request):
    req = json.loads(request.body)
    quiz_id = req['id']
    game_list = req['game_list']
    quiz_id = game_list.pop(0)
    game_list.append(quiz_id)
    type = req['type']

    if type == 'animal':
        quiz = BodyGame_animal.objects.get(id=quiz_id)
    elif type == 'food':
        quiz = BodyGame_food.objects.get(id=quiz_id)
    elif type == 'thing':
        quiz = BodyGame_thing.objects.get(id=quiz_id)
    elif type == 'job':
        quiz = BodyGame_job.objects.get(id=quiz_id)
    elif type == 'proverb':
        quiz = BodyGame_proverb.objects.get(id=quiz_id)

    word = quiz.word

    return JsonResponse({'id' : quiz_id, 'word' : word, 'game_list' : game_list})

def before_quiz(request):
    req = json.loads(request.body)
    quiz_id = req['id']
    game_list = req['game_list']

    next_quiz_id = game_list.pop()
    game_list.insert(0, next_quiz_id)
    quiz_id = game_list[-1]
    type = req['type']

    if type == 'animal':
        quiz = BodyGame_animal.objects.get(id=quiz_id)
    elif type == 'food':
        quiz = BodyGame_food.objects.get(id=quiz_id)
    elif type == 'thing':
        quiz = BodyGame_thing.objects.get(id=quiz_id)
    elif type == 'job':
        quiz = BodyGame_job.objects.get(id=quiz_id)
    elif type == 'proverb':
        quiz = BodyGame_proverb.objects.get(id=quiz_id)

    word = quiz.word
    
    return JsonResponse({'id' : quiz_id, 'word' : word, 'game_list' : game_list})