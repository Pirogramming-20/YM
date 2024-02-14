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
from ..lookInside.models import *

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
        form = LoginForm(request, request.POST)
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
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, template_name='main/login.html', context=context)
    
# @csrf_exempt
def logout(request):
    auth.logout(request)
    return redirect('main:main')

def answer(request,pk):
    figure_list=[]
    four_list=[]
    music_2000_list=[]
    music_2010_list=[]
    music_2020_list=[]
    movie_list=[]
    look_list=[]
    game=GameRoom.objects.get(pk=pk)
    name=game.room_name
    order_str=game.order_game
    order_list=order_str.split(",")
    for gn in order_list:
        if gn=='Figure':
            figure_random_str=game.ran_figure
            figure_id_list=list(map(int,figure_random_str.split(',')))
                    
            for figure_id in figure_id_list:
                f1=Figure.objects.get(id=figure_id)
                figure_list.append(f1.name)
        elif gn=='Four':
            four_random_str=game.ran_four
            four_id_list=list(map(int,four_random_str.split(',')))
            
            for four_id in four_id_list:
                f1=Four.objects.get(id=four_id)
                four_list.append(f1.answer)       
        elif gn=='Music':

            music_random_str=game.ran_music
            music_id_list=list(map(int,music_random_str.split(',')))
                    
            for music_id in music_id_list:
                f1=MusicGame_2000.objects.get(id=music_id)
                music_2000_list.append([f1.title,f1.singer])
            for music_id in music_id_list:
                f1=MusicGame_2010.objects.get(id=music_id)
                music_2010_list.append([f1.title,f1.singer])
            for music_id in music_id_list:
                f1=MusicGame_2020.objects.get(id=music_id)
                music_2020_list.append([f1.title,f1.singer])                                              
        elif gn=="Movie":
            movie_random_str=game.ran_movie
            movie_id_list=list(map(int,movie_random_str.split(',')))

            for movie_id in movie_id_list:
                f1=MovieGame.objects.get(id=movie_id)
                movie_list.append([f1.title,f1.line])
        elif gn=="Look":       
            look_random_str=game.ran_look
            look_id_list=list(map(int,look_random_str.split(',')))
            
            for look_id in look_id_list:
                f1=LookInside.objects.get(id=look_id)
                look_list.append(f1.name)
    
    
    ctx={
                'figure_answer':figure_list,  
                'movie_answer':movie_list,
                'four_answer':four_list,
                'music_2000_answer': music_2000_list,
                'music_2010_answer': music_2010_list,
                'music_2020_answer': music_2020_list,
                'look_answer':look_list,
                'room_name':name,
                'order_list':order_list,
    }    
    return render(request, 'main/answer_list.html', ctx)
        

    