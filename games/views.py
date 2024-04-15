from django.shortcuts import render
from .forms import Player1Form, Player2Form

# Create your views here.
def index(request):

    form1 = Player1Form()
    form2 = Player2Form()
    context = {
        'form1': form1,
        'form2': form2,
    }

    return render(request, 'games/index.html', context)