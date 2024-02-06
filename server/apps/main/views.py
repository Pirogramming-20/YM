from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
# from django.views.decorators.csrf import csrf_exempt
from ..chattings.models import *
from ..musicGames.models import *

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
            print(game)
            music_random=game.RandomMusic_get.all()
            music_list=[]
            for music in music_random:
                id=music['music_game_id']
                music_R=MusicGame.objects.get(id=id)
                music_list.append([music_R['title'], music_R['singer']])
            ctx={
                'music_list':music_list,   
            }
            return render(request, 'main/answer_list.html', ctx=ctx)
        except GameRoom.DoesNotExist:
            return render(request, 'main/answer.html')
        

    return render(request, 'main/answer.html')
    