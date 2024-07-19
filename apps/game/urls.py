from django.urls import path
from .views import *

app_name = 'game'

urlpatterns = [
    path('', main, name='main'),
    path('game/attack/', attack, name='attack'), 
    path('game/history/', game_history, name='game_history'), # 전적 (게임 리스트)
    path('game/<int:pk>/', game_detail, name='game_detail'),
    path('game/<int:pk>/counter/', counter_attack, name='counter_attack'),
    path('game/<int:pk>/cancel/', cancel_game, name='cancel_game'), # 게임 취소
    path('ranking/', ranking, name='ranking'),
]
