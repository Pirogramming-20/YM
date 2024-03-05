from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class SignupForm(UserCreationForm):
    username = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class' : 'signup-input'
            }
        )
    )        
    password1 = forms.CharField(
        label='비밀번호  ',
        widget=forms.PasswordInput(
            attrs={
                'class' : 'signup-input'
            }
        )
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={
                'class' : 'signup-input'
            }
        )
    )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',]
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class' : 'signup-input'
            }
        )
    ) 