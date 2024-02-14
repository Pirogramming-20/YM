from django.shortcuts import render, redirect
from apps.chattings.models import GameRoom
from . models import *
import random
from django.http import JsonResponse
import json

# Create your views here.
def body_game_main(request, roomId):
    quiz_data = [
        #동물
        {'type' : 'animal', 'word' : '토끼'},
        {'type' : 'animal', 'word' : '고양이'},
        {'type' : 'animal', 'word' : '강아지'},
        {'type' : 'animal', 'word' : '말'},
        {'type' : 'animal', 'word' : '쥐'},
        {'type' : 'animal', 'word' : '개구리'},
        {'type' : 'animal', 'word' : '닭'},
        {'type' : 'animal', 'word' : '호랑이'},
        {'type' : 'animal', 'word' : '사자'},
        {'type' : 'animal', 'word' : '원숭이'},
        {'type' : 'animal', 'word' : '코끼리'},
        {'type' : 'animal', 'word' : '늑대'},
        {'type' : 'animal', 'word' : '게'},
        {'type' : 'animal', 'word' : '펭귄'},
        {'type' : 'animal', 'word' : '거북이'},
        {'type' : 'animal', 'word' : '악어'},
        {'type' : 'animal', 'word' : '펭귄'},
        {'type' : 'animal', 'word' : '상어'},
        {'type' : 'animal', 'word' : '나무늘보'},
        {'type' : 'animal', 'word' : '목도리도마뱀'},
        {'type' : 'animal', 'word' : '캥거루'},
        {'type' : 'animal', 'word' : '오리'},
        {'type' : 'animal', 'word' : '코뿔소'},
        {'type' : 'animal', 'word' : '돌고래'},
        {'type' : 'animal', 'word' : '코알라'},
        {'type' : 'animal', 'word' : '고릴라'},
        {'type' : 'animal', 'word' : '타조'},
        {'type' : 'animal', 'word' : '기린'},
        {'type' : 'animal', 'word' : '문어'},
        {'type' : 'animal', 'word' : '곰'},
        #음식
        {'type' : 'food', 'word' : '치킨'},
        {'type' : 'food', 'word' : '김밥'},
        {'type' : 'food', 'word' : '아이스크림'},
        {'type' : 'food', 'word' : '햄버거'},
        {'type' : 'food', 'word' : '짜장면'},
        {'type' : 'food', 'word' : '빵'},
        {'type' : 'food', 'word' : '떡볶이'},
        {'type' : 'food', 'word' : '김치'},
        {'type' : 'food', 'word' : '바나나'},
        {'type' : 'food', 'word' : '레몬'},
        {'type' : 'food', 'word' : '포도'},
        {'type' : 'food', 'word' : '수박'},
        {'type' : 'food', 'word' : '라면'},
        {'type' : 'food', 'word' : '삼겹살'},
        {'type' : 'food', 'word' : '비빔밥'},
        {'type' : 'food', 'word' : '돼지국밥'},
        {'type' : 'food', 'word' : '산낙지'},
        {'type' : 'food', 'word' : '초밥'},
        {'type' : 'food', 'word' : '김치'},
        {'type' : 'food', 'word' : '회'},
        {'type' : 'food', 'word' : '군고구마'},
        {'type' : 'food', 'word' : '피자'},
        {'type' : 'food', 'word' : '마라탕'},
        {'type' : 'food', 'word' : '닭발'},
        {'type' : 'food', 'word' : '돈까스'},
        {'type' : 'food', 'word' : '탕후루'},
        {'type' : 'food', 'word' : '와플'},
        {'type' : 'food', 'word' : '샌드위치'},
        {'type' : 'food', 'word' : '도넛'},
        {'type' : 'food', 'word' : '파스타'},
        #물건
        {'type' : 'thing', 'word' : '열쇠'},
        {'type' : 'thing', 'word' : '옷장'},
        {'type' : 'thing', 'word' : '시계'},
        {'type' : 'thing', 'word' : '핸드폰'},
        {'type' : 'thing', 'word' : '신문'},
        {'type' : 'thing', 'word' : '소파'},
        {'type' : 'thing', 'word' : '에어컨'},
        {'type' : 'thing', 'word' : '선풍기'},
        {'type' : 'thing', 'word' : '청소기'},
        {'type' : 'thing', 'word' : '노트북'},
        {'type' : 'thing', 'word' : '창문'},
        {'type' : 'thing', 'word' : '카메라'},
        {'type' : 'thing', 'word' : '침대'},
        {'type' : 'thing', 'word' : '칫솔'},
        {'type' : 'thing', 'word' : '수건'},
        {'type' : 'thing', 'word' : '비누'},
        {'type' : 'thing', 'word' : '크레파스'},
        {'type' : 'thing', 'word' : '축구공'},
        {'type' : 'thing', 'word' : '스케치북'},
        {'type' : 'thing', 'word' : '우산'},
        {'type' : 'thing', 'word' : '목걸이'},
        {'type' : 'thing', 'word' : '장화'},
        {'type' : 'thing', 'word' : '가방'},
        {'type' : 'thing', 'word' : '책상'},
        {'type' : 'thing', 'word' : '의자'},
        {'type' : 'thing', 'word' : '휴지'},
        {'type' : 'thing', 'word' : '텀블러'},
        {'type' : 'thing', 'word' : '안경'},
        {'type' : 'thing', 'word' : '거울'},
        {'type' : 'thing', 'word' : '마우스'},
        #직업
        {'type' : 'job', 'word' : '마술사'},
        {'type' : 'job', 'word' : '경찰'},
        {'type' : 'job', 'word' : '요리사'},
        {'type' : 'job', 'word' : '소방관'},
        {'type' : 'job', 'word' : '간호사'},
        {'type' : 'job', 'word' : '프로게이머'},
        {'type' : 'job', 'word' : '개발자'},
        {'type' : 'job', 'word' : '모델'},
        {'type' : 'job', 'word' : '아나운서'},
        {'type' : 'job', 'word' : '의사'},
        {'type' : 'job', 'word' : '작가'},
        {'type' : 'job', 'word' : '피아니스트'},
        {'type' : 'job', 'word' : '변호사'},
        {'type' : 'job', 'word' : '배우'},
        {'type' : 'job', 'word' : '헬스 트레이너'},
        {'type' : 'job', 'word' : '영화 감독'},
        {'type' : 'job', 'word' : '댄서'},
        {'type' : 'job', 'word' : '농부'},
        {'type' : 'job', 'word' : '판사'},
        {'type' : 'job', 'word' : '지휘자'},
        {'type' : 'job', 'word' : '바리스타'},
        {'type' : 'job', 'word' : '사진작가'},
        {'type' : 'job', 'word' : '복서'},
        {'type' : 'job', 'word' : '수영 선수'},
        {'type' : 'job', 'word' : '농구 선수'},
        {'type' : 'job', 'word' : '야구 선수'},
        {'type' : 'job', 'word' : '화가'},
        {'type' : 'job', 'word' : '미용사'},
        {'type' : 'job', 'word' : '우주비행사'},
        {'type' : 'job', 'word' : '건축가'},
        #속담
        {'type' : 'proverb', 'word' : '지렁이도 밟으면 꿈틀한다'},
        {'type' : 'proverb', 'word' : '낫 놓고 ㄱ자도 모른다'},
        {'type' : 'proverb', 'word' : '낮말은 새가 듣고 밤말은 쥐가 듣는다'},
        {'type' : 'proverb', 'word' : '소 귀에 경 읽기'},
        {'type' : 'proverb', 'word' : '하룻강아지 범 무서운 줄 모른다'},
        {'type' : 'proverb', 'word' : '서당개 3년이면 풍월을 읊는다'},
        {'type' : 'proverb', 'word' : '윗물이 맑아야 아랫물이 맑다'},
        {'type' : 'proverb', 'word' : '등잔 밑이 어둡다'},
        {'type' : 'proverb', 'word' : '누워서 침 뱉기'},
        {'type' : 'proverb', 'word' : '누워서 떡 먹기'},
        {'type' : 'proverb', 'word' : '식은 죽 먹기'},
        {'type' : 'proverb', 'word' : '소 잃고 외양간 고치기'},
        {'type' : 'proverb', 'word' : '가는 말이 고와야 오는 말이 곱다'},
        {'type' : 'proverb', 'word' : '미운 놈 떡 하나 더 준다'},
        {'type' : 'proverb', 'word' : '작은 고추가 더 맵다'},
        {'type' : 'proverb', 'word' : '돌다리도 두들겨보고 건너라'},
        {'type' : 'proverb', 'word' : '세살 버릇 여든까지 간다'},
        {'type' : 'proverb', 'word' : '하늘이 무너져도 솟아날 구멍은 있다'},
        {'type' : 'proverb', 'word' : '티끌 모아 태산'},
        {'type' : 'proverb', 'word' : '발 없는 말이 천리 간다'},
        {'type' : 'proverb', 'word' : '시작이 반이다'},
        {'type' : 'proverb', 'word' : '백지장도 맞들면 낫다'},
        {'type' : 'proverb', 'word' : '바늘 가는데 실 간다'},
        {'type' : 'proverb', 'word' : '고래 싸움에 새우 등 터진다'},
        {'type' : 'proverb', 'word' : '원수는 외나무 다리에서 만난다'},
        {'type' : 'proverb', 'word' : '바늘 도둑이 소 도둑 된다'},
        {'type' : 'proverb', 'word' : '콩 심은 데 콩 나고 팥 심은 데 팥 난다'},
        {'type' : 'proverb', 'word' : '사공이 많으면 배가 산으로 간다'},
        {'type' : 'proverb', 'word' : '믿는 도끼에 발등 찍힌다'},
        {'type' : 'proverb', 'word' : '강 건너 불구경 하듯 한다'},
    ]

    for data in quiz_data:
        if data['type'] == 'animal':
            BodyGame_animal.objects.get_or_create(word=data['word'])
        elif data['type'] == 'food':
            BodyGame_food.objects.get_or_create(word=data['word'])
        elif data['type'] == 'thing':
            BodyGame_thing.objects.get_or_create(word=data['word'])
        elif data['type'] == 'job':
            BodyGame_job.objects.get_or_create(word=data['word'])
        elif data['type'] == 'proverb':
            BodyGame_proverb.objects.get_or_create(word=data['word'])
    
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