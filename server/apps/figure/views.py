from django.shortcuts import render
from .models import Figure, QuizFigure
import random

def create_figure_model():
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

    figures = Figure.objects.all()
    for figure in figures:
        figure.image_path = f"/static/image/figure/{figure.name}.jpg"
        figure.save()

def figure_quiz(request):
    create_figure_model()

    QuizFigure.objects.all().delete()

    quiz_id_list = random.sample(range(1,11), 5)

    for quiz_id in quiz_id_list:
        figure_instance = Figure.objects.get(id=quiz_id)
        QuizFigure.objects.create(figure_quiz_id=figure_instance)
    
    quiz_figures = QuizFigure.objects.all()
    quiz_figure = quiz_figures.first()
    ctx={
        'quiz_figure':quiz_figure
    }
    
    return render(request, "games/figure.html", ctx)

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def next_figure_ajax(request):
    req = json.loads(request.body)
    figure_id = int(req['id'])
    figure_id += 1

    figure = QuizFigure.objects.get(id=figure_id)
    image_path = figure.figure_quiz_id.image_path
    name = figure.figure_quiz_id.name

    return JsonResponse({'id':figure_id, 'image_path': image_path, 'name':name})