from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import SignUpForm, LoginForm,   ProfileSettingsForm
from .models import User
from django.views.generic import CreateView, FormView, TemplateView, UpdateView


# Create your views here.


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'pages/signup.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()  # Сохраняем пользователя
        return super().form_valid(form)





class LoginView(FormView):
    model = User
    form_class = LoginForm
    template_name = 'pages/signin.html'
    success_url = '/'

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = authenticate(username=username,
        email=email,password=password)

        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('home')
            else:
                return HttpResponse('User have been banned')
        else:
            return HttpResponse('Wrong data or user is not found')

def logout1(request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('home')




class UserpageView(TemplateView):
    template_name = 'pages/user_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = self.request.user
        return  context

class UserSettingsView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileSettingsForm
    template_name = 'pages/user_settings.html'
    success_url = reverse_lazy('user_page')

    def get_object(self, queryset=None):
         return self.request.user

    def form_valid(self, form):
        # Если форма валидна, сохраняем данные и выводим сообщение об успехе
        messages.success(self.request, "Ваши данные были успешно обновлены!")
        return super().form_valid(form)
class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'pages/change_password.html'
    success_url = reverse_lazy('user_page')  #

    def form_valid(self, form):
        messages.success(self.request, "Ваш пароль был успешно изменен!")
        return super().form_valid(form)