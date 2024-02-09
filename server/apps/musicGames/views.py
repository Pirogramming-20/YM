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
def music_game_main(request, roomId):
    quiz_data = [
        {'title': '벌써 일년', 'music': '/static/audio/music_game/2000/벌써 일년.mp3', 'singer': '브라운아이즈', 'youtube': 'https://www.youtube.com/embed/LZlIqfMn4cc?si=VbOb_tpc2xv4F-0A&amp;start=159'},
        {'title': '거짓말', 'music': '/static/audio/music_game/2000/거짓말.mp3', 'singer': '빅뱅', 'youtube': 'https://www.youtube.com/embed/NeDeZUqNiVo?si=LH8vkS1w_hsox6sG&amp;start=85'},
        {'title': 'I Don\'t Care', 'music': '/static/audio/music_game/2000/I Don\'t Care.mp3', 'singer': '투애니원', 'youtube': 'https://www.youtube.com/embed/4MgAxMO1KD0?si=cN50Tl5-Xu1ABOaS&amp;start=88'},
        {'title': 'Gee', 'music': '/static/audio/music_game/2000/Gee.mp3', 'singer': '소녀시대', 'youtube': 'https://www.youtube.com/embed/U7mPqycQ0tQ?si=-NwjsF9t0NZZoR50&amp;start=79'},
        {'title': 'Sorry Sorry', 'music': '/static/audio/music_game/2000/Sorry Sorry.mp3', 'singer': '슈퍼주니어', 'youtube': 'https://www.youtube.com/embed/x6QA3m58DQw?si=sk07LSUup9twcSaY&amp;start=78'},
        {'title': '아브라카다브라', 'music': '/static/audio/music_game/2000/아브라카다브라.mp3', 'singer': '브라운아이드걸스', 'youtube': 'https://www.youtube.com/embed/o4wJGWcHzVA?si=ECAQh-LgF1FUfoTk&amp;start=15'},
        {'title': '뚜두뚜두', 'music': '/static/audio/music_game/2010/뚜두뚜두.mp3', 'singer': '블랙핑크', 'youtube': 'https://www.youtube.com/embed/IHNzOHi8sJs?si=lBgvYpn4FXOn09uq&amp;start=76'},
        {'title': 'DNA', 'music': '/static/audio/music_game/2010/DNA.mp3', 'singer': '방탄소년단', 'youtube': 'https://www.youtube.com/embed/MBdVXkSdhwU?si=huPiie_CLxGDKClN&amp;start=87'},
        {'title': '오늘부터 우리는', 'music': '/static/audio/music_game/2010/오늘부터 우리는.mp3', 'singer': '여자친구', 'youtube': 'https://www.youtube.com/embed/YYHyAIFG3iI?si=LYheUvSriGcU2P8Z&amp;start=35'},
        {'title': 'Love Shot', 'music': '/static/audio/music_game/2010/Love Shot.mp3', 'singer': '엑소', 'youtube': 'https://www.youtube.com/embed/pSudEWBAYRE?si=kcMWvRQ96Ya9DGrV&amp;start=45'},
        {'title': 'Dance the Night Away', 'music': '/static/audio/music_game/2010/Dance the Night Away.mp3', 'singer': '트와이스', 'youtube': 'https://www.youtube.com/embed/Fm5iP0S1z9w?si=Ki7ZHH9iRcoFjmqx&amp;start=78'},
        {'title': 'MILLIONS', 'music': '/static/audio/music_game/2010/MILLIONS.mp3', 'singer': '위너', 'youtube': 'https://www.youtube.com/embed/PALjhRpnfbk?si=CuThJcwv2TmvfjLe&amp;start=62'},
        {'title': '빨간맛', 'music': '/static/audio/music_game/2010/빨간맛.mp3', 'singer': '레드벨벳', 'youtube': 'https://www.youtube.com/embed/WyiIGEHQP8o?si=cnKMlL3mp29kINjw&amp;start=62'},
        {'title': 'ETA', 'music': '/static/audio/music_game/2020/ETA.mp3', 'singer': '뉴진스', 'youtube':'https://www.youtube.com/embed/jOTfBlKSQYY?si=JTk8_6t8s4C2T1Ci&amp;start=70'},
        {'title': '파이팅 해야지', 'music': '/static/audio/music_game/2020/파이팅 해야지.mp3', 'singer': '부석순', 'youtube':'https://www.youtube.com/embed/mBXBOLG06Wc?si=fyyjoqEu0yQL4O9H&amp;start=46'},
        {'title': '사건의 지평선', 'music': '/static/audio/music_game/2020/사건의 지평선.mp3', 'singer': '윤하', 'youtube': 'https://www.youtube.com/embed/BBdC1rl5sKY?si=JUL3Fizzx7teDtvR&amp;start=95'},
        {'title': 'Drama', 'music': '/static/audio/music_game/2020/Drama.mp3', 'singer': '에스파', 'youtube': 'https://www.youtube.com/embed/D8VEhcPeSlc?si=gCguu-inj3xt1w9L&amp;start=57'},
        {'title': 'Not Shy', 'music': '/static/audio/music_game/2020/Not Shy.mp3', 'singer': '있지', 'youtube': 'https://www.youtube.com/embed/wTowEKjDGkU?si=wVwJgFY18rhP95q2&amp;start=81'},
        {'title': '낙하', 'music': '/static/audio/music_game/2020/낙하.mp3', 'singer': '악동뮤지션', 'youtube': 'https://www.youtube.com/embed/EtiPbWzUY9o?si=dFZJr_u-0xzn8TMB&amp;start=51'},
    ]
    room = GameRoom.objects.get(id=roomId)
    for data in quiz_data:
        MusicGame.objects.get_or_create(title=data['title'], music=data['music'], singer=data['singer'], youtube=data['youtube'])
    
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
    QuizList.objects.all().delete()
    room = GameRoom.objects.get(id=roomId)
    quiz_id_list = room.ran_music
    quiz_id_list = quiz_id_list[1:-1]
    quiz_id_str_list = quiz_id_list.split(", ")
    quiz_id_str_list = quiz_id_str_list[:count]
    quiz_id_int_list = [int(quiz_id_str) for quiz_id_str in quiz_id_str_list]

    music = MusicGame.objects.filter(music__contains='2000').first()

    for quiz_id in quiz_id_int_list:
        music_game = MusicGame.objects.filter(music__contains='2000').get(id=quiz_id+music.id - 1)
        QuizList.objects.get_or_create(music_game_id=music_game)

    quiz_list = QuizList.objects.all()
    quiz = quiz_list.first()
    ctx = {
        'quiz' : quiz,
        'roomId' : roomId,
        'room':room,
        'count' : count,
    }
    return render(request, 'musicGames/music_game_start_2000.html', ctx)

def music_game_start_2010(request, roomId, count):
    QuizList.objects.all().delete()
    room = GameRoom.objects.get(id=roomId)
    quiz_id_list = room.ran_music
    quiz_id_list = quiz_id_list[1:-1]
    quiz_id_str_list = quiz_id_list.split(", ")
    quiz_id_str_list = quiz_id_str_list[:count]
    quiz_id_int_list = [int(quiz_id_str) for quiz_id_str in quiz_id_str_list]

    music = MusicGame.objects.filter(music__contains='2010').first()

    for quiz_id in quiz_id_int_list:
        music_game = MusicGame.objects.filter(music__contains='2010').get(id=quiz_id+music.id - 1)
        QuizList.objects.get_or_create(music_game_id=music_game)

    quiz_list = QuizList.objects.all()
    quiz = quiz_list.first()
    ctx = {
        'quiz' : quiz,
        'roomId' : roomId,
        'room':room,
        'count' : count,
    }
    return render(request, 'musicGames/music_game_start_2000.html', ctx)

def music_game_start_2020(request, count,roomId):
    QuizList.objects.all().delete()
    room = GameRoom.objects.get(id=roomId)
    quiz_id_list = room.ran_music
    quiz_id_list = quiz_id_list[1:-1]
    quiz_id_str_list = quiz_id_list.split(", ")
    quiz_id_str_list = quiz_id_str_list[:count]
    quiz_id_int_list = [int(quiz_id_str) for quiz_id_str in quiz_id_str_list]

    music = MusicGame.objects.filter(music__contains='2020').first()

    for quiz_id in quiz_id_int_list:
        music_game = MusicGame.objects.filter(music__contains='2020').get(id=quiz_id+music.id-1)
        QuizList.objects.get_or_create(music_game_id=music_game)

    quiz_list = QuizList.objects.all()
    quiz = quiz_list.first()
    ctx = {
        'quiz' : quiz,
        'count' : count,
        'roomId' : roomId,
        'room':room
    }
    return render(request, 'musicGames/music_game_start_2000.html', ctx)

def next_quiz(request):
    req = json.loads(request.body)
    quiz_id = int(req['id'])
    quiz_id += 1

    quiz = QuizList.objects.get(id=quiz_id)
    title = quiz.music_game_id.title
    music = quiz.music_game_id.music
    singer = quiz.music_game_id.singer
    youtube = quiz.music_game_id.youtube

    return JsonResponse({'id' : quiz_id, 'music' : music, 'youtube' : youtube})

def answer(request):
    print("here")
    req = json.loads(request.body)
    quiz_id = int(req['id'])

    quiz = QuizList.objects.get(id=quiz_id)
    title = quiz.music_game_id.title
    singer = quiz.music_game_id.singer

    return JsonResponse({'id' : quiz_id, 'title' : title, 'singer' : singer})