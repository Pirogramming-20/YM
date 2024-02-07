from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
import random
# Create your views here.

def main(request):
  rooms = GameRoom.objects.all().order_by('id')
  ctx = {
    'rooms' : rooms
  }
  return render(request,'chattings/main.html',ctx)


def create(request):
  print("create받음")
  if request.method == 'POST':
    print("POSST받음")
    room = GameRoom.objects.create(
      room_name = request.POST["room_name"],
      order_game = request.POST["order_list"]
    )
    room = GameRoom.objects.get(id = room.id)
    order_game_list = room.order_game.split(",")
    print(room.order_game)
    for i in range(len(order_game_list)):
      for game in order_game_list:
        if game == "Figure":
          print('figure')
          ran_quiz_list = random.sample(range(1,21),20)#각 게임 자료수에 맞게 고치기
          room.ran_figure = ran_quiz_list
        elif game == "Four":
          print('four')
          ran_quiz_list = random.sample(range(1,30),20)
          room.ran_four = ran_quiz_list
        elif game == "Movie":
          print('movie')
          ran_quiz_list = random.sample(range(1,30),20)
          room.ran_movie = ran_quiz_list
        elif game == "Music":
          print('music')
          ran_quiz_list = random.sample(range(1,30),20)
          room.ran_music = ran_quiz_list

      room.save()
      
      roomId = room.id

      return redirect('detail/{}'.format(roomId))
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

def next_game(request, roomId):
  room = GameRoom.objects.get(id=roomId)
  ctx = {
    'roomId':roomId,
    'room':room
  }
  order_games = room.order_game.split(",")

  if order_games:
    current_game = order_games.pop(0)
    room.order_game = ','.join(s for s in order_games)
    room.save()
    if current_game == "Figure":
      # return render(request, "games/figure_main.html", ctx)
      return redirect("/figure/{}".format(roomId))
    if current_game == "Four":
      return redirect("/fourWords/{}".format(roomId))
      # return render(request, "games/fourWords_main.html", ctx)
    if current_game == "Movie":
      return redirect(f"/games/{roomId}/movie-game")
      # return render(request, "movieGames/movie_game_main.html", ctx)
    if current_game == "Music":
      return render(request, "musicGames/music_game_main.html", ctx)
    if not order_games:
      return render(request, "chattings/main.html", ctx)
    

# 유저닉네임  + 채팅방이름
# 채팅방 아이디값 -> 채팅방이름
# GameRoom 




import qrcode
def detail(request,pk):
  room = get_object_or_404(GameRoom, pk=pk)
  # 배포코드
  # qrimg = qrcode.make("http://hello.chattest.p-e.kr/chatting-room/detail-mobile/"+str(pk))
  # qrimg.save("/home/ubuntu/YM/server/staticfiles/image/qr{}.png".format(pk))
  # 로컬코드
  qrimg = qrcode.make("http://127.0.0.1:8000//chatting-room/detail-mobile/"+str(pk))
  qrimg.save("C:/Users/user/Desktop/YM/server/static/image/qrcode/qr{}.png".format(pk)) #각자 YM주소에 맞게 수정
  ctx = {
    "room" : room,
  }
  return render(request, "chattings/detail.html", ctx)


def detailMobile(request,pk):
  room = get_object_or_404(GameRoom, pk=pk)
  user = request.user.username
  ctx = {
    "room" : room,
    'username' : user
  }
  return render(request, "chattings/detailMobile.html", ctx)