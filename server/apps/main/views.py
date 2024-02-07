from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
# from django.views.decorators.csrf import csrf_exempt
from ..chattings.models import *
from ..musicGames.models import *
from ..figure.models import *
from ..movieGames.models import *
from ..fourWords.models import *

# Create your views here.

def main(request):
    if request.user.is_authenticated:
        return redirect('rooms:main')  # Use the name you've defined in your urls.py for chattings:main
    return render(request, "main/main.html")

# @csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('rooms:main')
        else:
            ctx={
                'form':form,
            }
            return render(request, 'main/signup.html',context=ctx) 
    else:
        form = SignupForm()
        context={
            'form': form,
        }
        return render(request, template_name='main/signup.html', context=context)
    

# @csrf_exempt
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('rooms:main')
        else:
            context = {
                'form': form,
            }
            return render(request, template_name='main/login.html', context=context)
    else:
        form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, template_name='main/login.html', context=context)
    
# @csrf_exempt
def logout(request):
    auth.logout(request)
    return redirect('main:main')

def answer(request):
    if request.method=="POST":
        print(request.POST['room_name'])
        name=request.POST['room_name']
        try:
            game=GameRoom.objects.get(room_name=name)
            figure_random_str=game.ran_figure
            figure_id_list=list(map(str,figure_random_str.split(',')))
            figure_list=[]
            for figure_id in figure_id_list:
                f1=Figure.objects.get(id=figure_id)
                figure_list.append(f1.name)
            
            four_random_str=game.ran_four
            four_id_list=list(map(str,four_random_str.split(',')))
            four_list=[]
            for four_id in four_id_list:
                f1=Four.objects.get(id=four_id)
                four_list.append(f1.answer)       

            music_random_str=game.ran_music
            music_id_list=list(map(str,music_random_str.split(',')))
            music_list=[]
            for music_id in music_id_list:
                f1=MusicGame.objects.get(id=music_id)
                music_list.append(f1.title)
                music_list.append(f1.singer)                   
                
            movie_random_str=game.ran_movie
            movie_id_list=list(map(str,movie_random_str.split(',')))
            movie_list=[]
            for movie_id in movie_id_list:
                f1=MovieGame.objects.get(id=movie_id)
                movie_list.append(f1.title)
                movie_list.append(f1.line)         
                     
            ctx={
                'figure_answer':figure_list,  
                'movie_answer':movie_list,
                'four_answer':four_list,
                'music_answer': music_list,
                'room_name':name,
            }
            return render(request, 'main/answer_list.html', ctx)
        except GameRoom.DoesNotExist:
            return render(request, 'main/answer.html')
        

    return render(request, 'main/answer.html')
    