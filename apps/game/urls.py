from django.urls import path
from .views import *

app_name = 'game'

urlpatterns = [
<<<<<<< HEAD
    path('', main, name='main'),
    path('game/attack/', attack, name='attack'), 
    path('game/history/', game_history, name='game_history'), # 전적 (게임 리스트)
    path('game/<int:pk>/', game_detail, name='game_detail'),
    path('game/<int:pk>/counter/', counter_attack, name='counter_attack'),
    path('game/<int:pk>/cancel/', cancel_game, name='cancel_game'), # 게임 취소
    path('ranking/', ranking, name='ranking'),
=======
    path('', views.main, name='main'),
    path('game-history/', views.game_history, name='game_history'), # 전적 페이지
    path('cancel-game/<int:game_id>/', views.cancel_game, name='cancel_game'), # 게임 취소
    path('counter-attack/<int:game_id>/', views.counter_attack, name='counter_attack'), # 반격하기
    path('game/<int:pk>/', views.game_detail, name='game_detail'),
    path('game/attack/', views.attack, name='attack'),
>>>>>>> feature/minsu
]
