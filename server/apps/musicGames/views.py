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
        {'title': 'Oh my Julia', 'music': '/static/audio/music_game/2000/Oh my Julia.mp3', 'singer': '컨츄리꼬꼬', 'youtube': "https://www.youtube.com/embed/Xbk_NStauds?si=4IqgIpYEeE8qC1aV&amp;start=52"},
        {'title': 'Fire', 'music': '/static/audio/music_game/2000/Fire.mp3', 'singer': '2NE1', 'youtube': "https://www.youtube.com/embed/49AfuuRbgGo?si=Y46jmf-NWWv0sLYi&amp;start=79"},
        {'title': '내 귀에 캔디', 'music': '/static/audio/music_game/2000/내 귀에 캔디.mp3', 'singer': '백지영(feat.택연 of 2PM)', 'youtube': "https://www.youtube.com/embed/rMG1YtxHLB8?si=Gd25xrnu-bQMnAqC&amp;start=57"},
        {'title': 'Heartbreaker', 'music': '/static/audio/music_game/2000/Heartbreaker.mp3', 'singer': '지드래곤', 'youtube': "https://www.youtube.com/embed/LOXEVd-Z7NE?si=TOoPpVxcqk6WzUUv&amp;start=44" },
        {'title': '길', 'music': '/static/audio/music_game/2000/길.mp3', 'singer': '지오디', 'youtube': "https://www.youtube.com/embed/OFlxQZNWNMU?si=HO0dFunuX4OcKWs-&amp;start=167"},
        {'title': 'I\'m sorry', 'music': '/static/audio/music_game/2000/I\'m sorry.mp3', 'singer': '거미(feat.T.O.P)', 'youtube': "https://www.youtube.com/embed/ERlf_9BW4iA?si=4sTTvS4MJu8gC5tR&amp;start=153"},
        {'title': '10 Minutes', 'music': '/static/audio/music_game/2000/10 Minutes.mp3', 'singer': '이효리', 'youtube': "https://www.youtube.com/embed/iKdr44yEBQU?si=1ztaFHZdcId6nk-L&amp;start=9"},
        {'title': 'So Hot', 'music': '/static/audio/music_game/2000/So Hot.mp3', 'singer': '원더걸스', 'youtube': "https://www.youtube.com/embed/lmun5PO54VE?si=T6A0yRBua7ch-BRf&amp;start=96"},
        {'title': '잊을게', 'music': '/static/audio/music_game/2000/잊을게.mp3', 'singer': '윤도현 밴드(YB)', 'youtube': "https://www.youtube.com/embed/VecH1Y2INho?si=Lp8cyaIzym1s3d2j&amp;start=71"},
        {'title': '비행기', 'music': '/static/audio/music_game/2000/비행기.mp3', 'singer': '거북이', 'youtube': "https://www.youtube.com/embed/q3outEcc-HE?si=DTxCmrgA10vL-Yng&amp;start=16"},
        {'title': '바람만바람만', 'music': '/static/audio/music_game/2000/바람만바람만.mp3', 'singer': '김종국,sg워너비', 'youtube': "https://www.youtube.com/embed/gEZHjx1RM9c?si=EJPyRnPZmdBXUu4j&amp;start=240"},
        {'title': '8282', 'music': '/static/audio/music_game/2000/8282.mp3', 'singer': '다비치', 'youtube': "https://www.youtube.com/embed/IwibOy34oAw?si=0S3-e2qwX8avvn8c&amp;start=240"},
        {'title': 'D.I.S.C.O', 'music': '/static/audio/music_game/2000/D.I.S.C.O.mp3', 'singer': '엄정화(feat.T.O.P)', 'youtube': "https://www.youtube.com/embed/QzD3ZTRuhbs?si=lRyVIXOkdqOA3Tob&amp;start=71"},
        {'title': '헤어지지못하는여자 떠나가지못하는남자', 'music': '/static/audio/music_game/2000/헤어지지못하는여자 떠나가지못하는남자.mp3', 'singer': '리쌍(feat.정인)', 'youtube': "https://www.youtube.com/embed/3rYL8AHJaTc?si=hYUbLaKhBAiGVk1o&amp;start=21"},
        {'title': '꿈에', 'music': '/static/audio/music_game/2000/꿈에.mp3', 'singer': '박정현', 'youtube': "https://www.youtube.com/embed/O5M2WFmFn04?si=8jvaAKlxooaiNdLc&amp;start=21"},
        {'title': '남자를 몰라', 'music': '/static/audio/music_game/2000/남자를 몰라.mp3', 'singer': '버즈', 'youtube': "https://www.youtube.com/embed/6n6UZpv50AU?si=sn1eGnWv1xTeyAah&amp;start=125"},
        {'title': '넘버원', 'music': '/static/audio/music_game/2000/넘버원.mp3', 'singer': '보아', 'youtube': "https://www.youtube.com/embed/ceZc-5p3g1w?si=3VSm1BsLmMDGEMzL&amp;start=40"},
        {'title': 'Love Story', 'music': '/static/audio/music_game/2000/Love Story.mp3', 'singer': '비(Rain)', 'youtube': "https://www.youtube.com/embed/2xnpFI3PLYs?si=xCuaA6eY4-1NWoHe&amp;start=310"},
        {'title': '유혹의 소나타', 'music': '/static/audio/music_game/2000/유혹의 소나타.mp3', 'singer': '아이비', 'youtube': "https://www.youtube.com/embed/Q_plceCKQX8?si=4JdG2CAFkUUClV63&amp;start=70"},
        {'title': '아시나요', 'music': '/static/audio/music_game/2000/아시나요.mp3', 'singer': '조성모', 'youtube': "https://www.youtube.com/embed/niiZThi8Eog?si=Pp8sa89ohzYfTHP0&amp;start=257"},
        {'title': '좋은 사람', 'music': '/static/audio/music_game/2000/좋은 사람.mp3', 'singer': '박효신', 'youtube': "https://www.youtube.com/embed/W7CcTfUu-mg?si=FLNku4H0EU_hOeyQ&amp;start=154"},
        {'title': '순정', 'music': '/static/audio/music_game/2000/순정.mp3', 'singer': '코요태', 'youtube': "https://www.youtube.com/embed/MHCBoNhQmCk?si=4fRwPzyCXsTGfz9y&amp;start=82"},
        {'title': '흔들린 우정', 'music': '/static/audio/music_game/2000/흔들린 우정.mp3', 'singer': '홍경민', 'youtube': "https://www.youtube.com/embed/SnGpl6AkvSY?si=W3NMrS11YqADEUZ1&amp;start=86"},
        {'title': '내 머리가 나빠서', 'music': '/static/audio/music_game/2000/내 머리가 나빠서.mp3', 'singer': 'SS501', 'youtube': "https://www.youtube.com/embed/kcKHzns0L5s?si=07uieZ-pNl6d8gA-&amp;start=86"},
        #2010
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
            return redirect('/games2/{0}/music-game/start-2000/{1}'.format(roomId,count))
        elif time == 2010:
            return redirect('/games2/{0}/music-game/start-2010/{1}'.format(roomId,count))
        elif time == 2020:
            return redirect('/games2/{0}/music-game/start-2020/{1}'.format(roomId,count))
        
    
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
    music_game_ids = random.sample(range(1, len(MusicGame.objects.filter(music__contains='2000')) + 1), count)
    music_game_query_2000 = MusicGame.objects.filter(music__contains='2000')
    first_music_2000 = music_game_query_2000.first()
    first_music_id_2000 = int(first_music_2000.id)
    room = GameRoom.objects.get(id=roomId)
    #만약에 년도가 섞여있는 상태로 테이블에 저장된다면... : 이 경우에 대해서 고민 필요
    for music_game_id in music_game_ids:
        music_game = MusicGame.objects.get(id=music_game_id + first_music_id_2000 - 1)
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
    music_game_ids = random.sample(range(1, len(MusicGame.objects.filter(music__contains='2010')) + 1), count)
    music_game_query_2000 = MusicGame.objects.filter(music__contains='2010')
    first_music_2000 = music_game_query_2000.first()
    first_music_id_2000 = int(first_music_2000.id)
    room = GameRoom.objects.get(id=roomId)
    #만약에 년도가 섞여있는 상태로 테이블에 저장된다면... : 이 경우에 대해서 고민 필요
    for music_game_id in music_game_ids:
        music_game = MusicGame.objects.get(id=music_game_id + first_music_id_2000 - 1)
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
    music_game_ids = random.sample(range(1, len(MusicGame.objects.filter(music__contains='2020')) + 1), count)
    music_game_query_2000 = MusicGame.objects.filter(music__contains='2020')
    first_music_2000 = music_game_query_2000.first()
    first_music_id_2000 = int(first_music_2000.id)
    room = GameRoom.objects.get(id=roomId)
    #만약에 년도가 섞여있는 상태로 테이블에 저장된다면... : 이 경우에 대해서 고민 필요
    for music_game_id in music_game_ids:
        music_game = MusicGame.objects.get(id=music_game_id + first_music_id_2000 - 1)
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