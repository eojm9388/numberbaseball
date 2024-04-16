from django.shortcuts import render, redirect
# from .forms import PlayerForm, PlayerNumForm
from .models import Player1, Player2
# Create your views here.

error_code = 0

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
        'turn': turn,
        'error_code': error_code,
    }
    print(error_code)
    return render(request, 'games/index.html', context)

def player1_number(request):    
    player1 = Player1(nickname=request.POST.get('nickname-player1'), number=request.POST.get('number-player1'))
    global error_code
    # 4자리 숫자가 아닌 경우
    if len(player1.number) != 4:
        error_code = 1
    # 중복된 숫자가 있을 경우
    elif len(set(player1.number)) != 4:
        error_code = 2
    # 정수가 아닌 값이 있을 경우
    elif not player1.number.isdigit():
        error_code = 3
    else:
        error_code = 0

    if error_code == 0:
        player1.save()
    
    return redirect('index')


def player2_number(request):    
    player2 = Player2(nickname=request.POST.get('nickname-player2'), number=request.POST.get('number-player2'))
    
    global error_code
    # 4자리 숫자가 아닌 경우
    if len(player2.number) != 4:
        error_code = 1
    # 중복된 숫자가 있을 경우
    elif len(set(player2.number)) != 4:
        error_code = 2
    # 정수가 아닌 값이 있을 경우
    elif not player2.number.isdigit():
        error_code = 3
    else:
        error_code = 0

    if error_code == 0:
        player2.save()

    return redirect('index')


def play_game(request):

    return render(request, 'games/playgame.html')