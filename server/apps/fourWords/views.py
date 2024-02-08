from django.shortcuts import render, redirect

from apps.chattings.models import GameRoom
from .models import Four, QuizFour
import random
import json
from django.http import JsonResponse

def fourWords_main(request,roomId):
    answer_list = ['샌드위치', '연지곤지', '차돌박이', '바리스타', '신속정확',
              '표고버섯', '대한민국', '급속충전', '양념치킨', '취중진담',
              '미세먼지', '드래곤볼', '십중팔구', '고진감래', '생로병사']
    
    for i in range(len(answer_list)):
        four_instance,created = Four.objects.get_or_create(answer=answer_list[i])
        four_instance.two_save()
    room = GameRoom.objects.get(id=roomId)
    ctx ={
        'roomId':roomId,
        'room':room
    }
    
    if request.method == "POST":
        count = int(request.POST.getlist('count')[0])
        ctx ={
            'roomId':roomId,
            'room':room,
            'count':count
        }
        return redirect('/fourWords/{0}/fourWords_game/{1}'.format(roomId,count))
    return render(request, 'games/fourWords_main.html',ctx)

def fourWords_game_start(request, roomId,count):
    
    QuizFour.objects.all().delete()

    quiz_id_list = random.sample(range(1,16), count)

    for quiz_id in quiz_id_list:
        four_instance = Four.objects.get(id=quiz_id)
        QuizFour.objects.create(four_quiz_id=four_instance)
    
    quiz_fours = QuizFour.objects.all()
    quiz_four = quiz_fours.first()
    room = GameRoom.objects.get(id=roomId)
    ctx={
        'quiz_four':quiz_four,
        'count': count,
        'roomId':roomId,
        'room':room
    }
    
    return render(request, "games/fourWords_start.html", ctx)

def next_fourWords_ajax(request):
    req = json.loads(request.body)
    four_id = int(req['id'])
    four_id += 1

    four = QuizFour.objects.get(id=four_id)
    two = four.four_quiz_id.two
    answer = four.four_quiz_id.answer

    return JsonResponse({'id':four_id, 'two': two})

def answer(request):
    req = json.loads(request.body)
    quiz_id = int(req['id'])

    quiz = QuizFour.objects.get(id=quiz_id)
    answer = quiz.four_quiz_id.answer

    return JsonResponse({'id' : quiz_id, 'answer' : answer})
