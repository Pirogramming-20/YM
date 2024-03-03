from django.shortcuts import render, redirect
from apps.chattings.models import GameRoom
from .models import Mudo
import random
import json
from django.http import JsonResponse

def mudo_main(request, roomId):#40개
    line_list = ['세브란스 병원엔 왜', '제발 가랑이 밑으로 들어가게 해주세요', '어 그래', '차씨 차씨 차씨 연예인을 대보자', '두 분은 연인이세요', '실례가 안 된다면 아이스크림 하나만 사주십시오', '해정발산기슭곰발냄새타령부인인사잘해',
                 '700만 대추인들이 만든거야', '싸브레', '북쪽에 계신', '차이나타운은 온통 빡빡이야', '필승 Yes I can', '아우 장난치지말고 빨리 자장면 주세요!!', '아버지 나를낳으시고 바지적삼 다적시셨네',
                 '늦었다고 생각할 때가 진짜 너무 늦었다', '입 닫고 빵이나 먹어', '장모 거세게 반데라스', '나온다 그랬더라 어떻게 됐더라', '농약 안 쳤을 걸', '야 남자가 무슨 빨간 머리냐', '날 동정하지 마세요', '나 이런 게 무서워하네', 
                 '하모예 와이러는데 이카는데', '우리 할아버진 할머니가 두 분이셨어', '무야호', '건방지게 끼어들었네요', '십 년이 지났다 주나야 년 뭐했냐', '인생을 판 사람을 어떻게 이겨요', '나 이제 그만할 건데', '스프', '술 마시고 뭘 타는지 보라고',
                 '치열하겠는데', '민서를 올바르게 키울 생각이 없다', '면일어나지 못했더라면', '특별히 공부도 못하고 대가리만 큰 사람', '아픈척해서 인기 끌려고 그러시는 거죠', '내가 뭣땜에 대체 뭘 위해서',
                 '700만 대추인들이 만든거야', '싸브레', '북쪽에 계신', '차이나타운은 온통 빡빡이야','오 진짜 별론데','그럼 하지마 이쒸','늦었다고 생각할 때가 진짜 너무 늦었다','됐어요! 피 수혈 안 해줘요', '망했어 재석이형 때문에', 
                 '바나나맛 우유 그만 먹으라고!!', '아유.. 하기 싫어','얘가 이기겠냐','와이프 하나 생겼나보다', '웃지마 민병관', '인기가 있어야 거품이지', '지나치게 얘기하라고 나오라고 한 거 아닙니까','치열하겠는데','형보다 잘할걸']
    for i in range(len(line_list)):
        Mudo.objects.get_or_create(line=line_list[i])
        mudo = Mudo.objects.get(line=line_list[i])
        mudo.image_path = f"/static/image/mudo/{mudo.line}.jpg"
        mudo.save()
    
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
        quiz_id_int_list = random.sample(range(1,21),count) #최대 20개
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