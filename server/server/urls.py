"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
handler404 = 'server.views.handler404'
handler500 = 'server.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("apps.main.urls")),
    path('figure/',include("apps.figure.urls")),
    path('fourWords/',include("apps.fourWords.urls")),
    path('lookInside/',include("apps.lookInside.urls")),
    path('chatting-room',include("apps.chattings.urls")),
    path('movie', include("apps.movieGames.urls")),
    path('music', include("apps.musicGames.urls")),
    path('body', include("apps.bodyGames.urls")),
    path('mudo', include("apps.mudoGames.urls")),
    path('chatGames/', include("apps.chatGames.urls")),
    
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root':settings.STATIC_ROOT}),

]
