from django import forms
from .models import VacancyAnswer

class VacancyAnswerForm(forms.ModelForm):
    class Meta:
        model = VacancyAnswer
        fields = ('name', 'lastname', 'surname', 'email', 'phone', 'birth_year', 'experience', 'city', 'diploma', 'text')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lastname'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),  # Исправлено
            'birth_year': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Birth Year', 'type': 'date'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Experience'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'diploma': forms.FileInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message'}),
        }
