from django.shortcuts import render

from apps.chattings.models import GameRoom
from .models import Four, QuizFour
import random
import json
from django.http import JsonResponse

def fourWords_main(request,roomId):
    answer_list = ['샌드위치', '연지곤지', '차돌박이', '바리스타', '신속정확', '표고버섯', '대한민국', '급속충전', '양념치킨', '취중진담',
              '미세먼지', '드래곤볼', '십중팔구', '고진감래', '생로병사', '선서유기', '흔들의자', '코카콜라', '삼시세끼', '브라우니', 
              '비트코인', '방방곡곡', '도원결의', '스파게티', '비타오백', '누네띠네', '어장관리', '버터구이', '업데이트', '카페베네',
              '붉은노을', '낄끼빠빠', '스타워즈', '백설공주', '오토바이', '파인애플', '스타필드', '사자성어', '비밀번호', '계좌번호',
              '생년월일', '고객센터', '알레르기', '현장학습', '뭉게구름', '호랑나비', '종이접기', '주의사항', '탄수화물', '삼각김밥',
              '소녀시대', '미끄럼틀', '원두커피', '하모니카', '신용카드', '타임오버', '하드캐리', '아카시아', '플라스틱', '마요네즈',]
    
    for i in range(len(answer_list)):
        four_instance,created = Four.objects.get_or_create(answer=answer_list[i])
        four_instance.two_save()
    room = GameRoom.objects.get(id=roomId)
    ctx ={
        'roomId':roomId,
        'room':room
    }
    
    return render(request, 'games/fourWords_main.html',ctx)

def fourWords_game_start(request, roomId):
    
    QuizFour.objects.all().delete()

    quiz_id_list = random.sample(range(1,16), 10)

    for quiz_id in quiz_id_list:
        four_instance = Four.objects.get(id=quiz_id)
        QuizFour.objects.create(four_quiz_id=four_instance)
    
    quiz_fours = QuizFour.objects.all()
    quiz_four = quiz_fours.first()
    room = GameRoom.objects.get(id=roomId)
    ctx={
        'quiz_four':quiz_four,
        'roomId':roomId,
        'room':room
    }
    
    return render(request, "games/fourWords_start.html", ctx)

def next_fourWords_ajax(request):
    req = json.loads(request.body)
    four_id = int(req['id'])
    four_id += 1

    four = QuizFour.objects.get(id=four_id)
    two = four.four_quiz_id.two
    answer = four.four_quiz_id.answer

    return JsonResponse({'id':four_id, 'two': two, 'answer':answer})
