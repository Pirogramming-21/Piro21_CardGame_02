from django.urls import path
from . import views
from .views import *

app_name = 'game'

urlpatterns = [
    path('', views.main, name='main'),
    path('game-history/', views.game_history, name='game_history'), # 전적 페이지
    path('cancel-game/<int:game_id>/', views.cancel_game, name='cancel_game'), # 게임 취소
    path('counter-attack/<int:game_id>/', views.counter_attack, name='counter_attack'), # 반격하기

]
