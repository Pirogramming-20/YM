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
def movie_game_main(request,roomId):#50개
    if roomId == 0:
        if request.method == "POST":
            count = int(request.POST['count'])
            ctx = {
            'roomId' : roomId,
            'count':count
            }
            return redirect('/movie/{0}/movie_game/{1}'.format(roomId,count))
        ctx = {
            'roomId' : roomId,
        }
        return render(request, 'movieGames/movie_game_main.html', ctx)

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
    # QuizList.objects.all().delete()    

    if(roomId == 0):
        quiz_id_int_list = random.sample(range(1,51),count)
        
    else:
        room = GameRoom.objects.get(id=roomId)
        quiz_id_list = room.ran_movie
        # quiz_id_list = quiz_id_list[1:-1]
        quiz_id_str_list = quiz_id_list.split(",")
        quiz_id_str_list = quiz_id_str_list[:count]
        quiz_id_int_list = [int(quiz_id_str) for quiz_id_str in quiz_id_str_list]

    movie_game = [(quiz_id_int_list[0])]
    for quiz_id in quiz_id_int_list[1:]:
        movie_game.append(quiz_id)
        # movie_game = MovieGame.objects.get(id=quiz_id)
        # QuizList.objects.get_or_create(movie_game_id=movie_game)



    quiz_id = movie_game.pop(0)
    movie_game.append(quiz_id)
    quiz = MovieGame.objects.get(id = quiz_id)

    if roomId == 0:
        ctx = {
        'quiz' : quiz,
        'roomId' : roomId,
        'count' : count,
        'movie_game' : movie_game,
        'quiz_id':quiz_id
        }
        return render(request, 'movieGames/movie_game_start.html', ctx)

    ctx = {
        'quiz' : quiz,
        'roomId' : roomId,
        'room':room,
        'count' : count,
        'movie_game' : movie_game,
        'quiz_id':quiz_id
    }
    return render(request, 'movieGames/movie_game_start.html', ctx)

def next_quiz(request):
    req = json.loads(request.body)
    quiz_id = (req['id'])
    game_list=(req['game_list'])
    quiz_id = game_list.pop(0)
    game_list.append(quiz_id)
    
    quiz = MovieGame.objects.get(id=quiz_id)
    scene = quiz.scene
    return JsonResponse({'id' : quiz_id, 'scene' : scene, 'game_list':game_list})

#이전문제
def before_quiz(request):
    req = json.loads(request.body)
    quiz_id = (req['id'])
    game_list=(req['game_list'])

    next_quiz_id = game_list.pop()
    game_list.insert(0,next_quiz_id)
    quiz_id = game_list[-1]

    quiz = MovieGame.objects.get(id=quiz_id)
    scene = quiz.scene
    return JsonResponse({'id' : quiz_id, 'scene' : scene, 'game_list':game_list})

def answer(request):
    req = json.loads(request.body)
    quiz_id = (req['id'])
    quiz = MovieGame.objects.get(id=quiz_id)
    title = quiz.title
    line = quiz.line

    return JsonResponse({'id' : quiz_id, 'title' : title, 'line' : line})