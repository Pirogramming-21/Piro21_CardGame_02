<<<<<<< HEAD
from django.urls import path
from .views import *

app_name = 'game'

urlpatterns = [
    path('', main, name='main'),
    path('attack/', attack, name='attack'),
]
=======
from django.urls import path
from .views import *
from . import views

app_name = 'game'

urlpatterns = [
    path('', main, name='main'),
    path('game/attack/', views.attack, name='attack'),
]
>>>>>>> 139da3ccd826d829b22e4166afb3e16dbb74cf98
