from django import forms
from .models import Player1, Player2

class Player1Form(forms.ModelForm):
    class Meta:
        model = Player1
        fields = ('nickname',)

class Player2Form(forms.ModelForm):
    class Meta:
        model = Player2
        fields = ('nickname',)
