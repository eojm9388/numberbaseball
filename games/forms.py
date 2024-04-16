from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('nickname1', 'nickname2')

class PlayerNumForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('number1', 'number2')


