# blog/urls.py
from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import signup, home

app_name = 'login'
urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat, name='chat'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('signup/', TemplateView.as_view(template_name='login/signup.html'), name='signup'),
]