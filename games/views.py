from django.shortcuts import render, redirect
# from .forms import PlayerForm, PlayerNumForm
from .models import Player1, Player2
# Create your views here.
def index(request):
    player1 = Player1.objects.all()
    player2 = Player2.objects.all()
    if len(player1) == 0:
        turn = 1
    elif len(player2) > 0:
        turn = 3
    else:
        turn = 2

    context = {
        'turn': turn
    }

    return render(request, 'games/index.html', context)

def player1_number(request):    
    player1 = Player1(nickname=request.POST.get('nickname-player1'), number=request.POST.get('number-player1'))
    player1.save()

    return redirect('index')

def player2_number(request):    
    player2 = Player2(nickname=request.POST.get('nickname-player2'), number=request.POST.get('number-player2'))
    player2.save()

    return redirect('index')

def create_player(request):

    if request.method == 'POST':
        form = PlayerForm(request.POST)
        form.save()

    return redirect('index')


def play_game(request):

    player_list = Player.objects.all()
    play_pk = len(player_list)
    player = Player.objects.get(pk=play_pk)

    context = {
        'player': player,
    }

    return render(request, 'games/playgame.html', context)



