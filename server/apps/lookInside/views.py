from django.shortcuts import render, redirect
from apps.chattings.models import GameRoom
from .models import *
import random
import json
from django.http import JsonResponse

def lookInside_main(request, roomId): #60개
    name_list = [
'목장갑','고무장갑','컵','텀블러','마우스','키보드','휴지','물티슈','가습기','베개','이불','빨래건조대','스탠드','젓가락','숟가락','전자레인지','가스레인지','부탄가스','책상','의자','연필','지우게','볼펜','노트북','핸드폰','지갑','토스트기','후라이팬','냄비','접시']
    for i in range(len(name_list)):
        LookInside.objects.get_or_create(name=name_list[i])
        lookInside = LookInside.objects.get(name=name_list[i])
        lookInside.image_path = f"/static/image/lookInside/{lookInside.name}.jpg"
        lookInside.save()

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
            return redirect('/lookInside/{0}/lookInside_game/{1}'.format(roomId,count))
        return render(request, "lookInside/lookInside_main.html",ctx)
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
        return redirect('/lookInside/{0}/lookInside_game/{1}'.format(roomId,count))
    return render(request, "lookInside/lookInside_main.html",ctx)

def lookInside_game_start(request,roomId,count):
    #채팅룸 랜덤 아이디랑 연결
    if roomId == 0:
        quiz_id_int_list = random.sample(range(1,31),count)
    else:
        room = GameRoom.objects.get(id=roomId)
        quiz_id_list = room.ran_look
        quiz_id_str_list = list(map(int, quiz_id_list.split(",")))
        quiz_id_int_list = quiz_id_str_list[:count]

    lookInside_game = [(quiz_id_int_list[0])]
    for quiz_id in quiz_id_int_list[1:]:
        lookInside_game.append(quiz_id)

    quiz_id = lookInside_game.pop(0)
    lookInside_game.append(quiz_id)
    quiz_lookInside = LookInside.objects.get(id = quiz_id)

    if roomId == 0:
        ctx={
        'quiz_lookInside':quiz_lookInside,
        'count' : count,
        'roomId' : roomId,
        'lookInside_game' : lookInside_game,
        'quiz_id':quiz_id
        }
        return render(request, "lookInside/lookInside_start.html", ctx)
    
    ctx={
        'quiz_lookInside':quiz_lookInside,
        'count' : count,
        'roomId' : roomId,
        'room':room,
        'lookInside_game' : lookInside_game,
        'quiz_id':quiz_id
    }
    
    return render(request, "lookInside/lookInside_start.html", ctx)

def next_lookInside_ajax(request):
    req = json.loads(request.body)
    quiz_id = (req['id'])
    game_list=(req['game_list'])
    quiz_id = game_list.pop(0)
    game_list.append(quiz_id)

    lookInside = LookInside.objects.get(id=quiz_id)
    image_path = lookInside.image_path

    return JsonResponse({'id':quiz_id, 'image_path': image_path, 'game_list':game_list})

def before_lookInside_ajax(request):
    req = json.loads(request.body)
    quiz_id = (req['id'])
    game_list=(req['game_list'])
  
    next_quiz_id = game_list.pop()
    game_list.insert(0,next_quiz_id)
    quiz_id = game_list[-1]

    lookInside = LookInside.objects.get(id=quiz_id)
    image_path = lookInside.image_path

    return JsonResponse({'id':quiz_id, 'image_path': image_path, 'game_list':game_list})

def answer(request):
    req = json.loads(request.body)
    quiz_id = (req['id'])

    quiz = LookInside.objects.get(id=quiz_id)
    name = quiz.name
    
    return JsonResponse({'id' : quiz_id, 'name' : name})