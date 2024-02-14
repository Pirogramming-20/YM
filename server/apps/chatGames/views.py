from django.shortcuts import render, redirect
from apps.chattings.models import GameRoom
from .models import *
import random
import json
from django.http import JsonResponse


#0. create figure db
#1. figure_game main page
def chatGames_main(request, roomId): #60개
    name_list = ['강다니엘', '강하늘', '거미', '고두심', '기안84', '김연아', '김연자','김우빈','나문희','노사연',
                 '다현', '디카프리오','라이언','마릴린먼로','모모','모차르트','문재인','박건후','박건후','박보검','방귀대장뿡뿡이',
                 '베토벤', '보아', '뿡뿡이', '세일러문', '세종대왕', '손흥민', '송가인', '송은이', '송중기', '아만다 사이프리드']
    for i in range(len(name_list)):
        ChatGame.objects.get_or_create(chatText=name_list[i])

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
            return redirect('/chatGames/{0}/chatGames_game/{1}'.format(roomId,count))
        return render(request, "chatGames/chatGames_main.html",ctx)

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
        return redirect('/chatGames/{0}/chatGames_game/{1}'.format(roomId,count))
    return render(request, "chatGames/chatGames_main.html",ctx)


def chatGames_game_start(request,roomId,count):
    #채팅룸 랜덤 아이디랑 연결
    if roomId == 0:
        quiz_id_int_list = random.sample(range(1,31),count)
    else:
        room = GameRoom.objects.get(id=roomId)
        quiz_id_list = room.ran_chat
        quiz_id_str_list = list(map(int, quiz_id_list.split(",")))
        quiz_id_int_list = quiz_id_str_list[:count]

    chatGames_game = [(quiz_id_int_list[0])]
    for quiz_id in quiz_id_int_list[1:]:
        chatGames_game.append(quiz_id)

    quiz_id = chatGames_game.pop(0)
    chatGames_game.append(quiz_id)
    quiz_chatGames = ChatGame.objects.get(id = quiz_id)

    if roomId == 0:
        ctx={
        'quiz_chatGames':quiz_chatGames,
        'count' : count,
        'roomId' : roomId,
        'chatGames_game' : chatGames_game,
        'quiz_id':quiz_id
        }
        return render(request, "chatGames/chatGames_start.html", ctx)
    
    ctx={
        'quiz_chatGames':quiz_chatGames,
        'count' : count,
        'roomId' : roomId,
        'room':room,
        'chatGames_game' : chatGames_game,
        'quiz_id':quiz_id
    }
    
    return render(request, "chatGames/chatGames_start.html", ctx)



def next_chatGames_ajax(request):
    req = json.loads(request.body)
    quiz_id = (req['id'])
    game_list=(req['game_list'])
    quiz_id = game_list.pop(0)
    game_list.append(quiz_id)

    chatText = ChatGame.objects.get(id=quiz_id)
    chatText = chatText.chatText

    return JsonResponse({'id':quiz_id,'chatText':chatText,  'game_list':game_list})



def before_chatGames_ajax(request):
    req = json.loads(request.body)
    quiz_id = (req['id'])
    game_list=(req['game_list'])
  
    next_quiz_id = game_list.pop()
    game_list.insert(0,next_quiz_id)
    quiz_id = game_list[-1]
    chatText = ChatGame.objects.get(id=quiz_id)
    chatText = chatText.chatText

    return JsonResponse({'id':quiz_id,'chatText':chatText,  'game_list':game_list})


