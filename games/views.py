from django.shortcuts import render, redirect
# from .forms import PlayerForm, PlayerNumForm
from .models import Player1, Player2, Expect1, Expect2
# Create your views here.

error_code = 0
turn_player = 1
end_game = False
games = 1

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
    
    if is_number(player1.number) == 0:
        player1.save()
    
    return redirect('index')


def player2_number(request):    
    player2 = Player2(nickname=request.POST.get('nickname-player2'), number=request.POST.get('number-player2'))
    
    if is_number(player2.number) == 0:
        player2.save()

    return redirect('index')


def play_game(request):
    expect1 = Expect1.objects.all()
    expect2 = Expect2.objects.all()

    context = {
        'turn_player': turn_player,
        'expect1': expect1,
        'expect2': expect2,
        'end_game': end_game,
    }
    print(end_game)
    return render(request, 'games/playgame.html', context)

def play_turn(request):
    global turn_player, end_game
    if request.method == 'POST':
        if turn_player == 1:
            expect_num = request.POST.get('expect1')
            if is_number(expect_num) == 0:
                turn_player = 2

                player = Player1.objects.get(pk=games)
                expect = Expect1(player=player, expect=expect_num)
                
                other_number = Player2.objects.get(pk=games).number

                strike, ball = strike_ball(other_number, expect_num)
                if not strike and not ball:
                    expect.status = 'OUT!'
                    expect.color = 'red'
                else:
                    expect.status = f'{strike}S {ball}B'
                    if strike == 4:
                        end_game = 1
                        return redirect('end_game')
                    elif strike > 0:
                        expect.color = 'blue'
                    else:
                        expect.color = 'green'

                expect.save()
                return redirect('play_game')

        elif turn_player == 2:
            expect_num = request.POST.get('expect2')
            if is_number(expect_num) == 0:
                turn_player = 1
                player = Player2.objects.get(pk=games)
                expect = Expect2(player=player, expect=expect_num)
                other_number = Player1.objects.get(pk=games).number

                strike, ball = strike_ball(other_number, expect_num)
                if not strike and not ball:
                    expect.status = 'OUT!'
                    expect.color = 'red'
                else:
                    expect.status = f'{strike}S {ball}B'
                    if strike == 4:
                        end_game = 2
                        return redirect('end_game')
                    if strike > 0:
                        expect.color = 'blue'
                    else:
                        expect.color = 'green'

                expect.save()
                return redirect('play_game')
    
    

def end_game(request):
    player1 = Player1.objects.get(pk=games)
    player2 = Player2.objects.get(pk=games)

    if end_game == 1:
        winner = player1.nickname
    else:
        winner = player2.nickname

    context = {
        'winner': winner,
        'player1': player1,
        'player2': player2,
    }

    return render(request, 'games/end_game.html', context)


def restart(request):
    global error_code, turn_player, end_game, games
    player1 = Player1.objects.get(pk=games)
    player2 = Player2.objects.get(pk=games)

    expect1 = Expect1.objects.all()
    expect2 = Expect2.objects.all()

    if request.method == 'POST':
        player1.delete()
        player2.delete()
        expect1.delete()
        expect2.delete()
        error_code = 0
        turn_player = 1
        end_game = False
        games += 1

    return redirect('index')


def strike_ball(number, expect):

    strike, ball = 0, 0

    for i in range(4):
        if number[i] == expect[i]:
            strike += 1
        elif number[i] in expect:
            ball += 1
    return strike, ball

def is_number(number):
    global error_code
    # 4자리 숫자가 아닌 경우
    if len(number) != 4:
        error_code = 1
    # 중복된 숫자가 있을 경우
    elif len(set(number)) != 4:
        error_code = 2
    # 정수가 아닌 값이 있을 경우
    elif not number.isdigit():
        error_code = 3
    else:
        error_code = 0
    
    return error_code