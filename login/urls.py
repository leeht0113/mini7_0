# blog/urls.py
from django.urls import path
from . import views

from .views import signup, home

app_name = 'login'
urlpatterns = [
    path('', views.index, name='index'),
    path('chat', views.chat, name='chat'),
    path('signup/', views.signup, name='signup'),
    path('home/', home, name='home'),
]
 