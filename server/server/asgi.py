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

   # 추가
site.addsitedir(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
# socketio.AsyncServer 인스턴스를 생성하고, 비동기식으로 작동하도록 설정
sio = socketio.AsyncServer(async_mode='asgi')
application = get_asgi_application()
asgi_app = get_asgi_application()
# name1 = 'a'
# room = ''
# userList = ''
# 이벤트 핸들러(연결)
@sio.event
async def connect(sid, environ):
    print('connect111111', sid)


@sio.event
async def join(sid, room_name):
    # global userList,name1,room
    # room = room_name
    # print(name1)
    # print('join')
    # name1 = username
    # userList += username
    # await sio.emit('joined',userList, room=room_name)
    
    # room.participants += 1
    # room.save()
    # room_count = room.participants
    print('join')
    await sio.enter_room(sid, room_name)
    
    

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
    # global userList,name1,room
    print('disconnect')

application = socketio.ASGIApp(sio, asgi_app)