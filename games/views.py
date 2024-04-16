from django.shortcuts import render, redirect
# from .forms import PlayerForm, PlayerNumForm
# from .models import Player
# Create your views here.
def index(request):
    
    

    return render(request, 'games/index.html')


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


def player1_number(request, game_pk):    
    player = Player(pk=game_pk)

    if request.method == 'POST':
        player.number1 = request.POST.get('play1-number')
        player.save()
    
    print(request.POST.get('play2-number'))
    return redirect('play_game')


def player2_number(request, game_pk):    
    player = Player(pk=game_pk)

    if request.method == 'POST':
        player.number2 = request.POST.get('play2-number')
        player.save()

    print(request.POST.get('play1-number'))
    return redirect('play_game')