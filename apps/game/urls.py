from django.urls import path
from .views import *

app_name = 'game'

urlpatterns = [
    path('', main, name='main'),
    path('game/<int:pk>/', game_detail, name='game_detail'),
]
