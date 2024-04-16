from django.shortcuts import render, redirect
# from .forms import PlayerForm, PlayerNumForm
from .models import Player1, Player2, Expect1, Expect2
# Create your views here.

error_code = 0
turn_player = 1

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
    player1_list = Player1.objects.all()
    player2_list = Player2.objects.all()
    player1_pk = len(player1_list)
    player2_pk = len(player2_list)
    player1 = Player1.objects.get(pk=player1_pk)
    player2 = Player2.objects.get(pk=player2_pk)
    expect1 = player1.expect_set.all()
    expect2 = player2.expect_set.all()

    context = {
        'player1': player1,
        'player2': player2,
        'expect1': expect1,
        'expect2': expect2,
    }

    return render(request, 'games/playgame.html', context)

def play_turn(request, expect_num):
    global turn_player
    if request.method == 'POST':
        if turn_player % 2:
            player1_list = Player1.objects.all()
            player1_pk = len(player1_list)
            player = Player1.objects.get(pk=player1_pk)
            expect = Expect1(player=player, expect=expect_num)
    
        else:
            player2_list = Player2.objects.all()
            player2_pk = len(player2_list)
            player = Player2.objects.get(pk=player2_pk)
            expect = Expect2(player=player, expect=expect_num)
        number = player.number
        number = [int(digit) for digit in number]
        expect_num = [int(digit) for digit in expect_num]
        strike, ball = strike_ball(number, expect_num)
        if not strike and not ball:
            expect.status = 'OUT!'
        else:
            expect.status = f'{strike}S {ball}B'
        expect.save()
    context = {
        'number': number,
        'expect': expect,
    }

    turn_player += 1
    
    return render(request, 'games/playgame.html', context)


def strike_ball(number, expect):
    strike, ball = 0, 0

    for i in range(4):
        if number[i] == expect[i]:
            strike += 1
        elif number[i] in expect:
            ball += 1
    return strike, ball

