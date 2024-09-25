from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic import TemplateView, ListView, DetailView
from .models import *
from .forms import *
from ..film.models import Film


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['film'] = Film.objects.all().order_by('-release')
        context['solofilm'] = Film.objects.first()
        context['allfilms'] = Film.objects.all().order_by('-raiting')
        return context


class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'


class AgreementView(TemplateView):
    template_name = 'pages/agreement.html'

class VacancyListView(ListView):
    model = Vacancy
    template_name = 'pages/vacancy_list.html'
    context_object_name = 'vacancies'
    queryset = Vacancy.objects.all()

    def get_queryset(self):

        search_text = self.request.GET.get('query')
        if search_text is None:
            return Vacancy.objects.all()
        q = self.model.objects.filter(
            Q(title__icontains=search_text) |
            Q(text__icontains=search_text)

        )
        return q

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.request.GET)
        return context


class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'pages/vacancy_detail.html'
    context_object_name = 'vacancy'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['form'] = VacancyAnswerForm()
        return context

    def post(self, request, *args, **kwargs):
        form = VacancyAnswerForm(request.POST, request.FILES)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.vacancy = self.get_object()
            answer.save()
            return redirect('vacancy_detail', pk=self.get_object().pk)
        return self.render_to_response(self.get_context_data(form=form))








