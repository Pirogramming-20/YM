from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
import random
import os
# Create your views here.

def main(request):
  print(request.user.id)
  
  rooms = GameRoom.objects.filter(user_id=request.user.id).order_by('id')
  
  ctx = {
    'rooms' : rooms
  }
  return render(request,'chattings/main.html',ctx)


def create(request):
  if request.method == 'POST':
    room_name = request.POST["room_name"]
    room_order = request.POST["order_list"]
    user=User.objects.get(id=request.user.id)
    if room_order !='':
      existing_room = GameRoom.objects.filter(room_name=room_name)
      if existing_room.exists():
        return render(request,'chattings/create.html', {'error':'error'})
      room = GameRoom.objects.create(
          room_name = request.POST["room_name"],
          order_game = request.POST["order_list"],
          user_id=user
        )
      room = GameRoom.objects.get(id = room.id)
      order_game_list = room.order_game.split(",")
      #게임 순서 필드
      order_num_list = list(range(len(order_game_list)))
      room.order_num = ','.join(map(str,order_num_list))
      for game in order_game_list:
          if game == "Figure": #1~30 사이 20개
            print('figure')
            ran_quiz_list = random.sample(range(1,61),15)#각 게임 자료수에 맞게 고치기
            ran_quiz_str=','.join(map(str,ran_quiz_list))###
            print(ran_quiz_str)
            room.ran_figure = ran_quiz_str
          elif game == "Four":
            print('four')
            ran_quiz_list = random.sample(range(1,51),15)#각 게임 자료수에 맞게 고치기
            ran_quiz_str=','.join(map(str,ran_quiz_list))
            room.ran_four = ran_quiz_str
          elif game == "Look":
            print('look')
            ran_quiz_list = random.sample(range(1,31),15)#각 게임 자료수에 맞게 고치기
            ran_quiz_str=','.join(map(str,ran_quiz_list))
            room.ran_look = ran_quiz_str
          elif game == "Movie":
            print('movie')
            ran_quiz_list = random.sample(range(1,51),15)#각 게임 자료수에 맞게 고치기
            ran_quiz_str=','.join(map(str,ran_quiz_list))
            room.ran_movie = ran_quiz_str
          elif game == "Mudo":
            print('mudo')
            ran_quiz_list = random.sample(range(1,41),15)#각 게임 자료수에 맞게 고치기
            ran_quiz_str=','.join(map(str,ran_quiz_list))
            room.ran_mudo = ran_quiz_str
          elif game == "Music":
            print('music')
            ran_quiz_list = random.sample(range(1,31),15)#각 게임 자료수에 맞게 고치기
            ran_quiz_str=','.join(map(str,ran_quiz_list))
            room.ran_music = ran_quiz_str
          elif game == "Body":
            print('body')
            ran_quiz_list = random.sample(range(1,31),15)#각 게임 자료수에 맞게 고치기
            ran_quiz_str=','.join(map(str,ran_quiz_list))
            room.ran_body = ran_quiz_str
          elif game == "Chat":
            print('chat')
            ran_quiz_list = random.sample(range(1,16),15)#각 게임 자료수에 맞게 고치기
            ran_quiz_str=','.join(map(str,ran_quiz_list))
            room.ran_chat = ran_quiz_str
      room.save()
      roomId = room.id
      
      return redirect('detail/{}'.format(roomId))
    else:
      return render(request, 'chattings/create.html', {'non_error':'error'})
  return render(request, 'chattings/create.html')

def next_game(request, roomId):
  if roomId == 0:
    return redirect('main:main')
  room = GameRoom.objects.get(id=roomId)
  ctx = {
    'roomId':roomId
  }
  order_games = room.order_game.split(",")
  if room.order_num:
    order_nums = list(map(int,room.order_num.split(',')))
    current_order = order_nums.pop(0)
    current_game = order_games[current_order]
    room.order_num = ','.join(map(str,order_nums))
    room.save()
    if current_game == "Figure":
      # return render(request, "games/figure_main.html", ctx) 
      return redirect("/figure/{}".format(roomId))
    elif current_game == "Four":
      return redirect("/fourWords/{}".format(roomId))
    elif current_game == "Look":
      return redirect("/lookInside/{}".format(roomId))
      # return render(request, "games/fourWords_main.html", ctx)
    elif current_game == "Movie":
      return redirect(f"/movie/{roomId}/")
      # return render(request, "movieGames/movie_game_main.html", ctx)
    elif current_game == "Mudo":
      return redirect("/mudo/{}".format(roomId))
      # return render(request, "games/mudo_main.html", ctx)
    elif current_game == "Music":
      return redirect(f"/music/{roomId}/")
      # return render(request, "musicGames/music_game_main.html", ctx)
    elif current_game == "Chat":
      return redirect(f"/chatGames/{roomId}")
      # return render(request, "musicGames/music_game_main.html", ctx)
    elif current_game == "Body":
      return redirect(f"/body/{roomId}/")
  else:
    return redirect(f"/chatting-room/finish/{roomId}", ctx)

def finish(request, roomId):
  print(roomId)
  room = GameRoom.objects.get(id=roomId)
  ctx = {
    'roomId':roomId
  }
  order_games = room.order_game.split(",") 
  return render(request, 'chattings/room_end.html',ctx)

#다시 게임 시작 => 게임 순서 필드 다시 생성
def re_game(request, roomId):
  room = GameRoom.objects.get(id=roomId)
  order_games = room.order_game.split(",")
  order_num_list = list(range(len(order_games)))
  room.order_num = ','.join(map(str,order_num_list))
  room.save()
  return redirect(f"/chatting-room/next_game/{roomId}")

# 둘 모두 삭제
def recreate(request, roomId):
  GameRoom.objects.get(id=roomId).delete()
  return redirect('/chatting-room/create')

def delete(request, roomId):
  GameRoom.objects.get(id=roomId).delete()
  image_path = os.path.join("/home/ubuntu/YM/server/staticfiles/image/",'qr{}.png'.format(roomId))
  if os.path.isfile(image_path):
        os.remove(image_path)
  return redirect('/chatting-room')
# 유저닉네임  + 채팅방이름
# 채팅방 아이디값 -> 채팅방이름
# GameRoom 




import qrcode
def detail(request,pk):
  room = get_object_or_404(GameRoom, pk=pk)
  # # 배포코드
  qrimg = qrcode.make("http://hello.chattest.p-e.kr/chatting-room/detail-mobile/"+str(pk))
  qrimg.save("/home/ubuntu/YM/server/staticfiles/image/qr{}.png".format(pk))

  # 로컬코드
  #qrimg = qrcode.make("http://127.0.0.1:8000//chatting-room/detail-mobile/"+str(pk))
  # qrimg.save("C:/Users/user/Desktop/YM/server/static/image/qrcode/qr{}.png".format(pk)) #기택
  #qrimg.save("C:/Users/chldb/YM/server/static/image/qrcode/qr{}.png".format(pk)) #윤서
  # qrimg.save("/Users/khinwaiyan/YM/server/static/image/qrcode/qr{}.png".format(pk)) #웨이
  # qrimg.save("C:/Users/cathy/OneDrive/바탕 화면/YM/YM/server/static/image/qrcode/qr{}.png".format(pk)) #현정
  # qrimg.save("C:/UOS/YM/server/static/image/qrcode/qr{}.png".format(pk)) #우진

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