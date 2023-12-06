# blog/urls.py
from django.urls import path
from . import views

from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

app_name = 'chatgpt'
urlpatterns = [
    path('', views.index, name='index'),
    path('chat', views.chat, name='chat'),
    path('resulttest', views.result_test),
    path('hj', views.index_hj, name='index_hj')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)