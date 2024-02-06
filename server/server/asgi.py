"""
ASGI config for server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""
# from apps.chattings.models import GameRoom
import os
from django.core.asgi import get_asgi_application
import socketio
   # 추가
import site
import django

# django.setup()
rooms = {}
   # 추가
site.addsitedir(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
# socketio.AsyncServer 인스턴스를 생성하고, 비동기식으로 작동하도록 설정
sio = socketio.AsyncServer(async_mode='asgi')
application = get_asgi_application()
asgi_app = get_asgi_application()

# 이벤트 핸들러(연결)
@sio.event
async def connect(sid, environ):
    print('connect111111', sid)
    

@sio.event
async def join(sid, room_name):
    await sio.enter_room(sid, room_name)
    if room_name in rooms:
        rooms[room_name] += 1  
    else:
        rooms[room_name] = 1 
    print(rooms[room_name])
    await sio.emit("count", rooms[room_name], room=room_name)  
    print('join')
    
    

@sio.event
async def leave(sid, room_name):
    # global userList
    # if userList in (' , ' + username):
    #     userList.replace((' , ' + username),'')
    # else:
    #     userList.replace((username+' , '),'')    
    # print('leave')
    # print(userList)
    print('leave')
    await sio.leave_room(sid, room_name)
    
@sio.event
async def message(sid, data,user,room_name):
    print('message ', data, user, room_name)
    await sio.emit('message', [data,user], room=room_name)

# 이벤트 핸들러(메세지 전송)
# @sio.event
# async def message(sid, data,user):
#     await sio.emit('message', [data,user])


# 이벤트 핸들러(연결 끊기)
@sio.event
async def disconnect(sid):
    for room_name in rooms:
        if sio.rooms(sid).__contains__(room_name):
            rooms[room_name] -= 1
            await sio.emit('count', rooms[room_name], room=room_name)
    print('disconnect')



application = socketio.ASGIApp(sio, application)