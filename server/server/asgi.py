"""
ASGI config for server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
import socketio


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
    print('connect2222222', sid)
    await sio.enter_room(sid, room_name)
    await sio.emit('joined', room=room_name)

@sio.event
async def leave(sid, room_name):
    await sio.leave_room(sid, room_name)
    await sio.emit('left', room=room_name)

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
    print('disconnect', sid)

application = socketio.ASGIApp(sio, asgi_app)