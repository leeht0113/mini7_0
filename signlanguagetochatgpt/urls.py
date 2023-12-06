# blog/urls.py
from django.urls import path
from . import views

app_name = 'signlanguagetochatgpt'
urlpatterns = [
    path('', views.index, name='index'),
    path('chat', views.chat, name='chat'),
    path('resulttest', views.result_test),
    path('chat2', views.chat2),
]
