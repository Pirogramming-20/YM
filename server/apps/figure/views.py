from django.shortcuts import render

from apps.chattings.models import GameRoom
from .models import Figure, QuizFigure
import random
import json
from django.http import JsonResponse


#0. create figure db
#1. figure_game main page
def figure_main(request, roomId): #20개
    Figure.objects.get_or_create(name="강다니엘")
    Figure.objects.get_or_create(name="강하늘")
    Figure.objects.get_or_create(name="거미")
    Figure.objects.get_or_create(name="고두심")
    Figure.objects.get_or_create(name="기안84")
    Figure.objects.get_or_create(name="김연아")
    Figure.objects.get_or_create(name="김연자")
    Figure.objects.get_or_create(name="김우빈")
    Figure.objects.get_or_create(name="나문희")
    Figure.objects.get_or_create(name="노사연")
    Figure.objects.get_or_create(name="다현")
    Figure.objects.get_or_create(name="디카프리오")
    Figure.objects.get_or_create(name="라이언")
    Figure.objects.get_or_create(name="마릴린먼로")
    Figure.objects.get_or_create(name="모모")
    Figure.objects.get_or_create(name="모차르트")
    Figure.objects.get_or_create(name="문재인")
    Figure.objects.get_or_create(name="박건후")
    Figure.objects.get_or_create(name="박보검")
    Figure.objects.get_or_create(name="방귀대장뿡뿡이")

    figures = Figure.objects.all()
    for figure in figures:
        figure.image_path = f"/static/image/figure/{figure.name}.jpg"
        figure.save()
    ctx = {
        'roomId' : roomId
    }
    return render(request, "games/figure_main.html",ctx)

def figure_game_start(request,roomId):

    QuizFigure.objects.all().delete()
    room = GameRoom.objects.get(id=roomId)
    quiz_id_list = room.ran_figure
    print(quiz_id_list)
    quiz_id_list = quiz_id_list[1:-1]
    quiz_id_str_list = quiz_id_list.split(", ")
    quiz_id_int_list = [int(quiz_id_str) for quiz_id_str in quiz_id_str_list]
    for quiz_id in quiz_id_int_list:
        figure_instance = Figure.objects.get(id=quiz_id)
        QuizFigure.objects.create(figure_quiz_id=figure_instance)

    quiz_figures = QuizFigure.objects.all()
    quiz_figure = quiz_figures.first()
    room1 = room.id
    ctx={
        'quiz_figure':quiz_figure,
        'roomId' : room1
    }
    
    return render(request, "games/figure_start.html", ctx)

def next_figure_ajax(request):
    req = json.loads(request.body)
    figure_id = int(req['id'])
    figure_id += 1

    figure = QuizFigure.objects.get(id=figure_id)
    image_path = figure.figure_quiz_id.image_path
    name = figure.figure_quiz_id.name

    return JsonResponse({'id':figure_id, 'image_path': image_path, 'name':name})