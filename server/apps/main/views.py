from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

# Create your views here.

def main(request):
    return render(request, "main/main.html")

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
    
    
def logout(request):
    auth.logout(request)
    return redirect('main:main')