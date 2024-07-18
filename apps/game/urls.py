from django.urls import path
from .views import *

app_name = 'game'

urlpatterns = [
    path('', main, name='main'),
    path('ranking/', ranking, name='ranking'),
    path('attack/', attack, name='attack'),
    path('counter/', counter, name='counter'),
    path('game/list/', game_list, name='game_list'),
    path('game/<int:pk>/', game_detail, name='game_detail'),
]