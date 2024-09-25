from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
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




class ProfileSettingsForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.SelectDateWidget(years=range(1900, 2025)),
        required=False
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'avatar', 'birth_date', 'city', 'gender', 'about']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }