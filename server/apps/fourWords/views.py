from django.shortcuts import render, redirect
from apps.chattings.models import GameRoom
from .models import Four
import random
import json
from django.http import JsonResponse

def fourWords_main(request,roomId):#50개
    if roomId ==0:
        ctx ={
            'roomId':roomId,
        }
        
        if request.method == "POST":
            count = int(request.POST['count'])
            ctx ={
                'roomId':roomId,
                'count':count
            }
            return redirect('/fourWords/{0}/fourWords_game/{1}'.format(roomId,count))
        return render(request, 'games/fourWords_main.html',ctx)
        
    room = GameRoom.objects.get(id=roomId)
    ctx ={
        'roomId':roomId,
        'room':room
    }
    
    if request.method == "POST":
        count = int(request.POST['count'])
        ctx ={
            'roomId':roomId,
            'room':room,
            'count':count
        }
        return redirect('/fourWords/{0}/fourWords_game/{1}'.format(roomId,count))
    return render(request, 'games/fourWords_main.html',ctx)

def fourWords_game_start(request, roomId,count):
    if roomId == 0:
        quiz_id_int_list = random.sample(range(1,51),count)
    else:
        room = GameRoom.objects.get(id=roomId)
        quiz_id_list = room.ran_four
        quiz_id_str_list = list(map(int,quiz_id_list.split(",")))
        quiz_id_int_list = quiz_id_str_list[:count]

    four_game = [(quiz_id_int_list[0])]
    for quiz_id in quiz_id_int_list[1:]:
        four_game.append(quiz_id)
    
    quiz_id = four_game.pop(0)
    four_game.append(quiz_id)
    quiz_four = Four.objects.get(id = quiz_id)

    if roomId == 0:
        ctx={
        'quiz_four':quiz_four,
        'count': count,
        'roomId':roomId,
        'four_game' : four_game,
        'quiz_id':quiz_id
        }
        return render(request, "games/fourWords_start.html", ctx)

    ctx={
        'quiz_four':quiz_four,
        'count': count,
        'roomId':roomId,
        'room':room,
        'four_game' : four_game,
        'quiz_id':quiz_id
    }
    
    return render(request, "games/fourWords_start.html", ctx)

def next_fourWords_ajax(request):
    req = json.loads(request.body)
    quiz_id = (req['id'])
    game_list=(req['game_list'])
    quiz_id = game_list.pop(0)
    game_list.append(quiz_id)

    four = Four.objects.get(id=quiz_id)
    two = four.two

    return JsonResponse({'id':quiz_id, 'two': two, 'game_list':game_list})

def before_fourWords_ajax(request):
    req = json.loads(request.body)
    quiz_id = (req['id'])
    game_list=(req['game_list'])

    next_quiz_id = game_list.pop()
    game_list.insert(0,next_quiz_id)
    quiz_id = game_list[-1]

    four = Four.objects.get(id=quiz_id)
    two = four.two

    return JsonResponse({'id':quiz_id, 'two': two, 'game_list':game_list})

def answer(request):
    req = json.loads(request.body)
    quiz_id = (req['id'])

    quiz = Four.objects.get(id=quiz_id)
    answer = quiz.answer

    return JsonResponse({'id' : quiz_id, 'answer' : answer})
