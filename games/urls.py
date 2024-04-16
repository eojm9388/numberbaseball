from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('play_game/', views.play_game, name='play_game'),
    path('play_turn/turn_player/', views.play_turn, name='play_turn'),
    path('player1_number/', views.player1_number, name='player1_number'),
    path('player2_number/', views.player2_number, name='player2_number'),
]