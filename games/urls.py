from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('create_player/', views.create_player, name='create_player'),
    # path('play_game/', views.play_game, name='play_game'),
    # path('player1_number/<int:game_pk>/', views.player1_number, name='player1_number'),
    # path('player2_number/<int:game_pk>/', views.player2_number, name='player2_number'),
]