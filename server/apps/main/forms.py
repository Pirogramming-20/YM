from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class' : 'signup-input'
            }
        )
    )
    password2 = forms.CharField(
        label='Password Confirm',
        widget=forms.PasswordInput(
            attrs={
                'class' : 'signup-input'
            }
        )
    )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',]