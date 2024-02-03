from django.shortcuts import render
from .models import *
import random
import json
from django.http import JsonResponse

# Create your views here.
# 0. mp3 파일 db에 저장
# 1-1. 전주 듣고 노래 맞추기 게임 표지 페이지
# 1-2. 전주 듣고 노래 맞추기 게임 규칙 설명
# 1-3. 년도 선택 : 2000년대 / 2010년대 / 2020년대
def music_game_main(request):
    quiz_data = [
        {'title': '벌써 일년', 'music': '/static/audio/music_game/2000/벌써 일년.mp3', 'singer': '브라운아이즈'},
        {'title': '거짓말', 'music': '/static/audio/music_game/2000/거짓말.mp3', 'singer': '빅뱅'},
        {'title': 'I Don\'t Care', 'music': '/static/audio/music_game/2000/I Don\'t Care.mp3', 'singer': '투애니원'},
        {'title': 'Gee', 'music': '/static/audio/music_game/2000/Gee.mp3', 'singer': '소녀시대'},
        {'title': 'Sorry Sorry', 'music': '/static/audio/music_game/2000/Sorry Sorry.mp3', 'singer': '슈퍼주니어'},
        {'title': '아브라카다브라', 'music': '/static/audio/music_game/2000/아브라카다브라.mp3', 'singer': '브라운아이드걸스'},
        {'title': '뚜두뚜두', 'music': '/static/audio/music_game/2010/뚜두뚜두.mp3', 'singer': '블랙핑크'},
        {'title': 'DNA', 'music': '/static/audio/music_game/2010/DNA.mp3', 'singer': '방탄소년단'},
        {'title': '오늘부터 우리는', 'music': '/static/audio/music_game/2010/오늘부터 우리는.mp3', 'singer': '여자친구'},
        {'title': 'Love Shot', 'music': '/static/audio/music_game/2010/Love Shot.mp3', 'singer': '엑소'},
        {'title': 'Dance the Night Away', 'music': '/static/audio/music_game/2010/Dance the Night Away.mp3', 'singer': '트와이스'},
        {'title': 'MILLIONS', 'music': '/static/audio/music_game/2010/MILLIONS.mp3', 'singer': '위너'},
        {'title': '빨간맛', 'music': '/static/audio/music_game/2010/빨간맛.mp3', 'singer': '레드벨벳'},
        {'title': 'ETA', 'music': '/static/audio/music_game/2020/ETA.mp3', 'singer': '뉴진스'},
        {'title': '파이팅 해야지', 'music': '/static/audio/music_game/2020/파이팅 해야지.mp3', 'singer': '부석순'},
        {'title': '사건의 지평선', 'music': '/static/audio/music_game/2020/사건의 지평선.mp3', 'singer': '윤하'},
        {'title': 'Drama', 'music': '/static/audio/music_game/2020/Drama.mp3', 'singer': '에스파'},
        {'title': 'Not Shy', 'music': '/static/audio/music_game/2020/Not Shy.mp3', 'singer': '있지'},
        {'title': '낙하', 'music': '/static/audio/music_game/2020/낙하.mp3', 'singer': '악동뮤지션'},
    ]

    for data in quiz_data:
        MusicGame.objects.get_or_create(title=data['title'], music=data['music'], singer=data['singer'])
    
    return render(request, 'musicGames/music_game_main.html')


# 2. 첫 문제 보여주는 페이지
# 3. 다음 버튼 눌렀을 때 : ajax로 구현
# 4. 우선 게임 종료 시 게임 표지 페이지로 이동 : ajax로 구현
def music_game_start_2000(request):
    QuizList.objects.all().delete()
    music_game_ids = random.sample(range(1, len(MusicGame.objects.filter(music__contains='2000')) + 1), 5)
    music_game_query_2000 = MusicGame.objects.filter(music__contains='2000')
    first_music_2000 = music_game_query_2000.first()
    first_music_id_2000 = int(first_music_2000.id)

    #만약에 년도가 섞여있는 상태로 테이블에 저장된다면... : 이 경우에 대해서 고민 필요
    for music_game_id in music_game_ids:
        music_game = MusicGame.objects.get(id=music_game_id + first_music_id_2000 - 1)
        QuizList.objects.get_or_create(music_game_id=music_game)

    quiz_list = QuizList.objects.all()
    quiz = quiz_list.first()
    ctx = {
        'quiz' : quiz,
    }
    return render(request, 'musicGames/music_game_start_2000.html', ctx)

def music_game_start_2010(request):
    QuizList.objects.all().delete()
    music_game_ids = random.sample(range(1, len(MusicGame.objects.filter(music__contains='2010')) + 1), 5)
    music_game_query_2000 = MusicGame.objects.filter(music__contains='2010')
    first_music_2000 = music_game_query_2000.first()
    first_music_id_2000 = int(first_music_2000.id)

    #만약에 년도가 섞여있는 상태로 테이블에 저장된다면... : 이 경우에 대해서 고민 필요
    for music_game_id in music_game_ids:
        music_game = MusicGame.objects.get(id=music_game_id + first_music_id_2000 - 1)
        QuizList.objects.get_or_create(music_game_id=music_game)

    quiz_list = QuizList.objects.all()
    quiz = quiz_list.first()
    ctx = {
        'quiz' : quiz,
    }
    return render(request, 'musicGames/music_game_start_2000.html', ctx)

def music_game_start_2020(request):
    QuizList.objects.all().delete()
    music_game_ids = random.sample(range(1, len(MusicGame.objects.filter(music__contains='2020')) + 1), 5)
    music_game_query_2000 = MusicGame.objects.filter(music__contains='2020')
    first_music_2000 = music_game_query_2000.first()
    first_music_id_2000 = int(first_music_2000.id)

    #만약에 년도가 섞여있는 상태로 테이블에 저장된다면... : 이 경우에 대해서 고민 필요
    for music_game_id in music_game_ids:
        music_game = MusicGame.objects.get(id=music_game_id + first_music_id_2000 - 1)
        QuizList.objects.get_or_create(music_game_id=music_game)

    quiz_list = QuizList.objects.all()
    quiz = quiz_list.first()
    ctx = {
        'quiz' : quiz,
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

    return JsonResponse({'id' : quiz_id, 'title' : title, 'music' : music, 'singer' : singer})