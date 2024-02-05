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
    # Tony: 패스워드 2개를 입력받을 필요 없이, 클라이언트에서 동일한 지 확인하면 될 것 같습니다.
    # Tony: 서버에서 이걸 확인할 경우 데이터 비용 낭비가 발생합니다.
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',]