from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from .models import User
from django.views.generic import CreateView, FormView


# Create your views here.


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'pages/signup.html'
    success_url = '/'



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
                return  redirect('home')
            else:
                return HttpResponse('User have been banned')
        else:
            return HttpResponse('Wrong data or user is not found')

def logout1(request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('home')
