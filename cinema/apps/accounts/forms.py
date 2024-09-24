from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username',
               'class':'form-styling'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email',
               'class':'form-styling'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password',
               'class':'form-styling'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password',
               'class':'form-styling'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username',
               'class':'form-styling'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email',
               'class': 'form-styling'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password',
               'class': 'form-styling'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password')