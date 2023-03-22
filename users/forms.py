from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import CustomUser

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'row'}))
    email = forms.EmailField(label='e-Mail', widget=forms.EmailInput(attrs={'class': 'row'}))
    city = forms.CharField(label='Город', widget=forms.TextInput(attrs={'class': 'row'}))
    street = forms.CharField(label='Улица', widget=forms.TextInput(attrs={'class': 'row'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'row'}))
    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput(attrs={'class': 'row'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'city', 'street', 'password1', 'password1')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'row'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'row'}))