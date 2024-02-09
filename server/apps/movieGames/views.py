from django.shortcuts import render, redirect

from apps.chattings.models import GameRoom
from .models import *
import random
import json
from django.http import JsonResponse
from apps.chattings.models import GameRoom

# Create your views here.

# 0. 영화 명대사 db에 create 하는 함수
# 1-1. 영화 명대사 게임 표지 페이지
# 1-2. 영화 명대사 게임 규칙 설명
def movie_game_main(request,roomId):
    quiz_data = [
        {'title': '1987', 'scene': '/static/image/movie_game/1987.png', 'line': '책상을 탁 치니 억 하고 쓰러졌답니다'},
        {'title': '관상', 'scene': '/static/image/movie_game/관상.png', 'line': '어찌 내가 왕이 될 상인가?'},
        {'title': '극한직업', 'scene': '/static/image/movie_game/극한직업.png', 'line': '지금까지 이런 맛은 없었다. 이것은 갈비인가 통닭인가. 예~ 수원왕갈비통닭입니다.'},
        {'title': '기생충', 'scene': '/static/image/movie_game/기생충.png', 'line': '제시카 외동딸 일리노이 시카고 과 선배는 김진모 그는 네 사촌'},
        {'title': '달콤한인생', 'scene': '/static/image/movie_game/달콤한인생.png', 'line': '넌 나에게 모욕감을 줬어'},
        {'title': '말죽거리잔혹사', 'scene': '/static/image/movie_game/말죽거리잔혹사.png', 'line': '니가 그렇게 싸움을 잘해?'},
        {'title': '범죄도시', 'scene': '/static/image/movie_game/범죄도시.png', 'line': '어 아직 싱글이야'},
        {'title': '범죄와의전쟁', 'scene': '/static/image/movie_game/범죄와의전쟁.png', 'line': '느그 서장 남천동 살제? 내가 임마! 느그 서장이랑 임마!'},
        {'title': '암살', 'scene': '/static/image/movie_game/암살.png', 'line': '내 몸 속에 일본놈들의 총알이 여섯개나 박혀 있습니다'},
        {'title': '더글로리', 'scene': '/static/image/movie_game/더글로리.png', 'line': '화이팅 박연지! 브라보! 멋지다 연진아~'},
        {'title': '타짜', 'scene': '/static/image/movie_game/타짜.png', 'line': '싸늘하다 가슴에 비수가 날아와 꽂힌다'},
        {'title': '살인의 추억', 'scene': '/static/image/movie_game/살인의 추억.png', 'line': '밥은 먹고 다니냐?'},
        {'title': '어게인 마이 라이프', 'scene': '/static/image/movie_game/어게인 마이 라이프.png', 'line': '진행시켜'},
        {'title': '천국의 계단', 'scene': '/static/image/movie_game/천국의 계단.png', 'line': '사랑은, 돌아오는 거야!'},
        {'title': '야인시대', 'scene': '/static/image/movie_game/야인시대.png', 'line': '내가, 내가 고자라니!'},
        {'title': '상속자들', 'scene': '/static/image/movie_game/상속자들.png', 'line': '나, 너 좋아하냐?'},
        {'title': '친구', 'scene': '/static/image/movie_game/친구.png', 'line': '아부지 뭐하시노'},
        {'title': '박하사탕', 'scene': '/static/image/movie_game/박하사탕.png', 'line': '나 다시 돌아갈래~'},
        {'title': '내 머리속의 지우개', 'scene': '/static/image/movie_game/내 머리속의 지우개.png', 'line': '이거 마시면 나랑 사귀는 거다'},
        {'title': '말아톤', 'scene': '/static/image/movie_game/말아톤.png', 'line': '초원이 다리는 백만 불 짜리 다리'},
        {'title': '타짜2', 'scene': '/static/image/movie_game/타짜2.png', 'line': '쏠 수 있어!'},
        {'title': '부부의 세계', 'scene': '/static/image/movie_game/부부의 세계.png', 'line': '사랑에 빠진 게 죄는 아니잖아!'},
        {'title': '아이리스', 'scene': '/static/image/movie_game/아이리스.png', 'line': '아악 안돼'},
        {'title': '신세계', 'scene': '/static/image/movie_game/신세계.png', 'line': '드루와, 드루와!'},
        {'title': '추격자', 'scene': '/static/image/movie_game/추격자.png', 'line': '야 4885, 너지?'},
        {'title': '파리의 연인', 'scene': '/static/image/movie_game/파리의 연인.png', 'line': '말을 못 해, 저 남자가 내 사람이다. 저 남자가 내 애인이다 왜 말을 못 하냐고!'},
        {'title': '오로라 공주', 'scene': '/static/image/movie_game/오로라 공주.png', 'line': '암세포도 생명이잖아요'},
        {'title': '베테랑', 'scene': '/static/image/movie_game/베테랑.png', 'line': '어이가 없네?'},
        {'title': '엽기적인 그녀', 'scene': '/static/image/movie_game/엽기적인 그녀.png', 'line': '견우야, 미안해! 나도 어쩔 수 없는 여자인가봐'},
        {'title': '내부자들', 'scene': '/static/image/movie_game/내부자들.png', 'line': '모히또 가가지고 몰디브나 한 잔 할라니까'},
        {'title': '곡성', 'scene': '/static/image/movie_game/곡성.png', 'line': '뭣이 중헌디'},
        {'title': '오징어 게임', 'scene': '/static/image/movie_game/오징어 게임.png', 'line': '하, 씨발⋯ 기훈이형!'},
        {'title': '아저씨', 'scene': '/static/image/movie_game/아저씨.png', 'line': '아직 한 발 남았다'},
        {'title': '지붕뚫고 하이킥', 'scene': '/static/image/movie_game/지붕뚫고 하이킥.png', 'line': '이 빵꾸똥꾸야!'},
        {'title': '올드보이', 'scene': '/static/image/movie_game/올드보이.png', 'line': '누구냐, 넌'},
        {'title': '모래시계', 'scene': '/static/image/movie_game/모래시계.png', 'line': '이렇게 하면 널 가질 수 있을 거라 생각했어'},
        {'title': '아저씨2', 'scene': '/static/image/movie_game/아저씨2.png', 'line': '나 전당포 한다, 금이빨은 받아. 금이빨 빼고 모조리 씹어먹어줄게'},
        {'title': '친구2', 'scene': '/static/image/movie_game/친구2.png', 'line': '니가 가라 하와이'},
        {'title': '신세계2', 'scene': '/static/image/movie_game/신세계2.png', 'line': '이러면 완전히 나가린데..'},
        {'title': '친구3', 'scene': '/static/image/movie_game/친구3.png', 'line': '마이 무따 아이가, 고마 해라'},
        {'title': '최고의 사랑', 'scene': '/static/image/movie_game/최고의 사랑.png', 'line': '극뽁~'},
        {'title': '태조 왕건', 'scene': '/static/image/movie_game/태조 왕건.png', 'line': '누구인가? 누가 기침소리를 내었는가?'},
        {'title': '부당거래', 'scene': '/static/image/movie_game/부당거래.png', 'line': '호의가 계속 되면, 그게 권리인 줄 알아요'},
        {'title': '봄날은 간다', 'scene': '/static/image/movie_game/봄날은 간다.png', 'line': '어떻게 사랑이 변하니...'},
        {'title': '달콤한 인생2', 'scene': '/static/image/movie_game/달콤한 인생2.png', 'line': '말해봐요, 나한테 왜 그랬어요?'},
        {'title': '말죽거리 잔혹사2', 'scene': '/static/image/movie_game/말죽거리 잔혹사2.png', 'line': '현수야, 이것 좀 만져 봐'},
        {'title': '내부자들2', 'scene': '/static/image/movie_game/내부자들2.png', 'line': '어짜피 대중들은 개 돼지입니다'},
        {'title': '다모', 'scene': '/static/image/movie_game/다모.png', 'line': '아프냐, 나도 아프다'},
        {'title': '청년경찰', 'scene': '/static/image/movie_game/청년경찰.png', 'line': '야 내가 소고기 사줄게'},
        {'title': '사랑했나봐', 'scene': '/static/image/movie_game/사랑했나봐.png', 'line': '예나... 선정이 딸이에요'},
    ]

    for data in quiz_data:
        MovieGame.objects.get_or_create(title=data['title'], scene=data['scene'], line=data['line'])

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
        return redirect('/movie/{0}/movie_game/{1}'.format(roomId,count))
    return render(request, 'movieGames/movie_game_main.html', ctx)

# 2. 영화 장면 보여주는 페이지
# 3. 다음 버튼 눌렀을 때 어떻게 할 건지 생각... : ajax로 구현
def movie_game_start(request,roomId, count):
    QuizList.objects.all().delete()    
    room = GameRoom.objects.get(id=roomId)
    quiz_id_list = room.ran_movie
    # quiz_id_list = quiz_id_list[1:-1]
    print("quiz_id_list",quiz_id_list)
    quiz_id_str_list = quiz_id_list.split(",")
    print("quiz_id_str_list_split",quiz_id_str_list)
    quiz_id_str_list = quiz_id_str_list[:count]

    quiz_id_int_list = [int(quiz_id_str) for quiz_id_str in quiz_id_str_list]

    for quiz_id in quiz_id_int_list:
        movie_game = MovieGame.objects.get(id=quiz_id)
        QuizList.objects.get_or_create(movie_game_id=movie_game)

    quiz_list = QuizList.objects.all()
    quiz = quiz_list.first()
    ctx = {
        'quiz' : quiz,
        'roomId' : roomId,
        'room':room,
        'count' : count
    }
    return render(request, 'movieGames/movie_game_start.html', ctx)

def next_quiz(request):
    req = json.loads(request.body)
    quiz_id = int(req['id'])
    quiz_id += 1

    quiz = QuizList.objects.get(id=quiz_id)
    scene = quiz.movie_game_id.scene

    return JsonResponse({'id' : quiz_id, 'scene' : scene})

def answer(request):
    req = json.loads(request.body)
    quiz_id = int(req['id'])

    quiz = QuizList.objects.get(id=quiz_id)
    title = quiz.movie_game_id.title
    line = quiz.movie_game_id.line

    return JsonResponse({'id' : quiz_id, 'title' : title, 'line' : line})