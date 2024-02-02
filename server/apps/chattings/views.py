from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
# Create your views here.

def main(request):
  rooms = GameRoom.objects.all().order_by('id')
  ctx = {
    'rooms' : rooms
  }
  return render(request,'chattings/main.html',ctx)


def create(request):
  if request.method == 'POST':
    form = RoomForm(request.POST)
    if form.is_valid():
      room = form.save(commit=False) 
      room.created_by = request.user  
      room.save() 
      
      return redirect('rooms:main')
    else:
      ctx={
        'room':form,
      }
      return render(request, 'chattings/create.html',ctx)
  else:
    room = RoomForm()
    ctx={
        'room': room,
    }
    return render(request, 'chattings/create.html', ctx)







def chatroom(request,pk):
  room = get_object_or_404(GameRoom, pk=pk)
  ctx = {
    "room" : room,
  }
  return render(request, "chattings/chatroom.html", ctx)


def choose(request,pk):
  room = get_object_or_404(GameRoom, pk=pk)
  ctx = {
    "room" : room,
  }
  return render(request, "chattings/choose.html")