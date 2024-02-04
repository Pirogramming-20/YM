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



from PIL import Image
import qrcode
def detail(request,pk):
  room = get_object_or_404(GameRoom, pk=pk)
  qrimg = qrcode.make("http://hello.chattest.p-e.kr/chatting-room/detail-mobile/"+str(pk))
  qrimg.save("/home/ubuntu/YM/server/staticfiles/image/qr.png")

  ctx = {
    "room" : room,
  }

  return render(request, "chattings/detail.html", ctx)


def detailMobile(request,pk):
  room = get_object_or_404(GameRoom, pk=pk)
  ctx = {
    "room" : room,
  }
  return render(request, "chattings/detailMobile.html", ctx)