from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import *

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'


class AgreementView(TemplateView):
    template_name = 'pages/agreement.html'

class VacancyListView(ListView):
    model = Vacancy
    template_name = 'pages/vacancy_list.html'
    context_object_name = 'vacancy'
    queryset = Vacancy.objects.all()

class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'pages/vacancy_detail.html'
    context_object_name = 'vacancy_detail'







