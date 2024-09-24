from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic import TemplateView, ListView, DetailView
from .models import *
from .forms import *

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
    context_object_name = 'vacancies'
    queryset = Vacancy.objects.all()




class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'pages/vacancy_detail.html'
    context_object_name = 'vacancy'

    def get_context_data(self, **kwargs):
        # Получаем существующий контекст из родительского класса
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст форму для ответа на вакансию
        context['form'] = VacancyAnswerForm()
        return context

    def post(self, request, *args, **kwargs):
        # Обрабатываем отправку формы с данными
        form = VacancyAnswerForm(request.POST, request.FILES)
        if form.is_valid():
            # Сохраняем ответ на вакансию
            answer = form.save(commit=False)
            answer.vacancy = self.get_object()  # Привязываем ответ к текущей вакансии
            answer.save()
            # Перенаправляем пользователя на ту же страницу вакансии после успешной отправки
            return redirect('vacancy_detail', pk=self.get_object().pk)
        # Если форма невалидна, отображаем страницу с формой и ошибками
        return self.render_to_response(self.get_context_data(form=form))








