from django.shortcuts import render
from .models import *
import random
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.

# 0. 영화 명대사 db에 create 하는 함수
# 1-1. 영화 명대사 게임 표지 페이지
# 1-2. 영화 명대사 게임 규칙 설명
def movie_game_main(request):
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
        {'title': '청년경찰', 'scene': '/static/image/movie_game/청년경찰.png', 'line': '야 내가 소고기 사줄게'},
    ]

    for data in quiz_data:
        MovieGame.objects.get_or_create(title=data['title'], scene=data['scene'], line=data['line'])

    # movie_game_ids = random.sample(range(1, len(quiz_data) + 1), 10)
    # movie_game_query = MovieGame.objects.all()
    # first_movie = movie_game_query.first()
    # first_movie_id = int(first_movie.id)

    # for movie_game_id in movie_game_ids:
    #     movie_game = MovieGame.objects.get(id=movie_game_id+first_movie_id-1)
    #     QuizList.objects.get_or_create(movie_game_id=movie_game)
    
    return render(request, 'movieGames/movie_game_main.html')

# 2. 영화 장면 보여주는 페이지
# 3. 다음 버튼 눌렀을 때 어떻게 할 건지 생각... : ajax로 구현
def movie_game_start(request):
    QuizList.objects.all().delete()
    movie_game_ids = random.sample(range(1, len(MovieGame.objects.all()) + 1), 10)
    movie_game_query = MovieGame.objects.all()
    first_movie = movie_game_query.first()
    first_movie_id = int(first_movie.id)

    for movie_game_id in movie_game_ids:
        movie_game = MovieGame.objects.get(id=movie_game_id+first_movie_id-1)
        QuizList.objects.get_or_create(movie_game_id=movie_game)

    quiz_list = QuizList.objects.all()
    quiz = quiz_list.first()
    ctx = {
        'quiz' : quiz,
    }
    return render(request, 'movieGames/movie_game_start.html', ctx)

@csrf_exempt
def next_quiz(request):
    req = json.loads(request.body)
    quiz_id = int(req['id'])
    quiz_id += 1

    quiz = QuizList.objects.get(id=quiz_id)
    scene = quiz.movie_game_id.scene
    title = quiz.movie_game_id.title
    line = quiz.movie_game_id.line

    return JsonResponse({'id' : quiz_id, 'scene' : scene, 'title' : title, 'line' : line})