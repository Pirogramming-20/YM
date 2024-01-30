from django import forms

from .models import *

class RoomForm(forms.ModelForm):
    
    class Meta:
        model = GameRoom
        fields = ('room_name',)