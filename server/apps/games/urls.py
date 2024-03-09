from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name='games'

urlpatterns = [
    path('',main,name = 'main'),
    path('',image,name = 'image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)