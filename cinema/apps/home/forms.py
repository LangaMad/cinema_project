from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import VacancyAnswer
class VacancyAnswerForm(UserCreationForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Name',
               'class':'form-control'}))
    lastname = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Lastname',
               'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email',
               'class':'form-control'}))
    phone = forms.CharField(widget=forms.CharField(
        attrs={'placeholder': 'Phone',
               'class':'form-control'}))
    birth_year = forms.DateField(widget=forms.DateInput(
        attrs={'placeholder': 'Birth_year',
               'class': 'form-control'}))
    experience = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Experience',
               'class': 'form-control'}))
    city = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'City',
               'class': 'form-control'}))
    diploma = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Diploma',
               'class': 'form-control'}))
    text = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Text',
               'class': 'form-control'}))


    class Meta:
        model = VacancyAnswer
        fields = ('name','lastname', 'email', 'phone', 'birth_year','experience','city','diploma', "text")