from django.shortcuts import render
from .models import Figure, QuizFigure
import random
import json
from django.http import JsonResponse


#0. create figure db
#1. figure_game main page
def figure_main(request): #20개
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
    
    return render(request, "games/figure_main.html")

def figure_game_start(request,roomId):

    QuizFigure.objects.all().delete()

    quiz_id_list = random.sample(range(1,21), 10)

    for quiz_id in quiz_id_list:
        figure_instance = Figure.objects.get(id=quiz_id)
        QuizFigure.objects.create(figure_quiz_id=figure_instance)

    quiz_figures = QuizFigure.objects.all()
    quiz_figure = quiz_figures.first()
    ctx={
        'quiz_figure':quiz_figure
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