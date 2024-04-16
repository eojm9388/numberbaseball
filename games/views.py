from django.shortcuts import render, redirect
from .forms import PlayerForm, PlayerNumForm
# Create your views here.
def index(request):

    form = PlayerForm()
    
    context = {
        'form': form,
    }

    return render(request, 'games/index.html', context)


def create_player(request):

    if request.method == 'POST':
        form = PlayerForm(request.POST)
        form.save()

    return redirect('index')


def play_game(request):
    
    return render(request, 'games/playgame.html')