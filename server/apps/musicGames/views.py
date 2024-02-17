from django.shortcuts import render, redirect
from apps.chattings.models import GameRoom
from .models import *
import random
import json
from django.http import JsonResponse

# Create your views here.
# 0. mp3 파일 db에 저장
# 1-1. 전주 듣고 노래 맞추기 게임 표지 페이지
# 1-2. 전주 듣고 노래 맞추기 게임 규칙 설명
# 1-3. 년도 선택 : 2000년대 / 2010년대 / 2020년대
def music_game_main(request, roomId):#30개씩
    if roomId == 0:
        if request.method == 'POST':
            count = int(request.POST['count'])
            time = int(request.POST['time'])
            ctx = {
            'roomId' : roomId,
            'count':count
            }
            
            if time == 2000:
                return redirect('/music/{0}/music_game_2000/{1}'.format(roomId,count))
            elif time == 2010:
                return redirect('/music/{0}/music_game_2010/{1}'.format(roomId,count))
            elif time == 2020:
                return redirect('/music/{0}/music_game_2020/{1}'.format(roomId,count))
        ctx = {
            'roomId' : roomId,
            }
        return render(request, 'musicGames/music_game_main.html', ctx)

    room = GameRoom.objects.get(id=roomId)
    if request.method == 'POST':
        count = int(request.POST['count'])
        time = int(request.POST['time'])
        ctx = {
        'roomId' : roomId,
        'room':room,
        'count':count
        }
        
        if time == 2000:
            return redirect('/music/{0}/music_game_2000/{1}'.format(roomId,count))
        elif time == 2010:
            return redirect('/music/{0}/music_game_2010/{1}'.format(roomId,count))
        elif time == 2020:
            return redirect('/music/{0}/music_game_2020/{1}'.format(roomId,count))
        
    
    ctx = {
        'roomId' : roomId,
        'room':room,
        }
    return render(request, 'musicGames/music_game_main.html', ctx)


# 2. 첫 문제 보여주는 페이지
# 3. 다음 버튼 눌렀을 때 : ajax로 구현
# 4. 우선 게임 종료 시 게임 표지 페이지로 이동 : ajax로 구현
def music_game_start_2000(request, roomId, count):
    if(roomId == 0):
        quiz_id_int_list = random.sample(range(1,31),count)
    else:
        room = GameRoom.objects.get(id=roomId)
        quiz_id_list = room.ran_music
        quiz_id_str_list = list(map(int,quiz_id_list.split(",")))
        quiz_id_int_list = quiz_id_str_list[:count]
    
    music = MusicGame_2000.objects.all()
    music_game = [music[quiz_id_int_list[0]-1].id]
    for quiz_id in quiz_id_int_list[1:]:
        music_game_now =music[quiz_id-1].id
        music_game.append(music_game_now)

    quiz_id = music_game.pop(0)
    music_game.append(quiz_id)
    quiz = MusicGame_2000.objects.get(id = quiz_id)

    if roomId == 0:
        ctx = {
        'quiz' : quiz,
        'roomId' : roomId,
        'count' : count,
        'music_game' : music_game,
        'year' : '2000',
        }
        return render(request, 'musicGames/music_game_start_2000.html', ctx)
    ctx = {
        'quiz' : quiz,
        'roomId' : roomId,
        'room':room,
        'count' : count,
        'music_game' : music_game,
        'year' : '2000',
    }
    return render(request, 'musicGames/music_game_start_2000.html', ctx)

def music_game_start_2010(request, roomId, count):
    if(roomId == 0):
        quiz_id_int_list = random.sample(range(1,31),count)
    else:
        room = GameRoom.objects.get(id=roomId)
        quiz_id_list = room.ran_music
        quiz_id_str_list = list(map(int,quiz_id_list.split(",")))
        quiz_id_int_list = quiz_id_str_list[:count]

    
    music = MusicGame_2010.objects.all()
    music_game = [music[quiz_id_int_list[0]-1].id]
    for quiz_id in quiz_id_int_list[1:]:
        music_game_now =music[quiz_id-1].id
        music_game.append(music_game_now)


    quiz_id = music_game.pop(0)
    music_game.append(quiz_id)
    quiz = MusicGame_2010.objects.get(id = quiz_id)

    if roomId == 0:
        ctx = {
        'quiz' : quiz,
        'count' : count,
        'roomId' : roomId,
        'music_game' : music_game,
        'year' : '2010',
        }
        return render(request, 'musicGames/music_game_start_2000.html', ctx)

    ctx = {
        'quiz' : quiz,
        'roomId' : roomId,
        'room':room,
        'count' : count,
        'music_game' : music_game,
        'year' : '2010',
    }
    return render(request, 'musicGames/music_game_start_2000.html', ctx)

def music_game_start_2020(request, count,roomId):
    if(roomId == 0):
        quiz_id_int_list = random.sample(range(1,31),count)
    else:
        room = GameRoom.objects.get(id=roomId)
        quiz_id_list = room.ran_music
        quiz_id_str_list = list(map(int,quiz_id_list.split(",")))
        quiz_id_int_list = quiz_id_str_list[:count]

    music = MusicGame_2020.objects.all()
    music_game = [music[quiz_id_int_list[0]-1].id]
    for quiz_id in quiz_id_int_list[1:]:
        music_game_now =music[quiz_id-1].id
        music_game.append(music_game_now)

    quiz_id = music_game.pop(0)
    music_game.append(quiz_id)
    quiz = MusicGame_2020.objects.get(id = quiz_id)

    if roomId == 0:
        ctx = {
        'quiz' : quiz,
        'count' : count,
        'roomId' : roomId,
        'music_game' : music_game,
        'year' : '2020',
        }
        return render(request, 'musicGames/music_game_start_2000.html', ctx)

    ctx = {
        'quiz' : quiz,
        'count' : count,
        'roomId' : roomId,
        'room':room,
        'music_game' : music_game,
        'year' : '2020',
    }
    return render(request, 'musicGames/music_game_start_2000.html', ctx)

def next_quiz(request):
    req = json.loads(request.body)
    quiz_id = (req['id'])
    game_list=(req['game_list'])
    quiz_id = game_list.pop(0)
    game_list.append(quiz_id)
    year = int(req['year'])

    if year == 2000:
        quiz = MusicGame_2000.objects.get(id=quiz_id)
    elif year == 2010:
        quiz = MusicGame_2010.objects.get(id=quiz_id)
    elif year == 2020:
        quiz = MusicGame_2020.objects.get(id=quiz_id)

    music = quiz.music
    youtube = quiz.youtube

    return JsonResponse({'id' : quiz_id, 'music' : music, 'youtube' : youtube, 'game_list':game_list})


def before_quiz(request):
    req = json.loads(request.body)
    quiz_id = (req['id'])
    game_list=(req['game_list'])

    next_quiz_id = game_list.pop()
    game_list.insert(0,next_quiz_id)
    quiz_id = game_list[-1]
    year = int(req['year'])

    if year == 2000:
        quiz = MusicGame_2000.objects.get(id=quiz_id)
    elif year == 2010:
        quiz = MusicGame_2010.objects.get(id=quiz_id)
    elif year == 2020:
        quiz = MusicGame_2020.objects.get(id=quiz_id)

    music = quiz.music
    youtube = quiz.youtube

    return JsonResponse({'id' : quiz_id, 'music' : music, 'youtube' : youtube, 'game_list':game_list})

def answer(request):
    print("here")
    req = json.loads(request.body)
    quiz_id = (req['id'])
    year = int(req['year'])

    if year == 2000:
        quiz = MusicGame_2000.objects.get(id=quiz_id)
    elif year == 2010:
        quiz = MusicGame_2010.objects.get(id=quiz_id)
    elif year == 2020:
        quiz = MusicGame_2020.objects.get(id=quiz_id)
        
    title = quiz.title
    singer = quiz.singer

    return JsonResponse({'id' : quiz_id, 'title' : title, 'singer' : singer})