from django.urls import path
from .views import *
from . import views

app_name = 'game'

urlpatterns = [
    path('', main, name='main'),
    path('game/attack/', views.attack, name='attack'),
]
