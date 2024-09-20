
from django.views.generic import ListView, DetailView

from .models import *
from django.shortcuts import render

from ..celebrities.models import Celebrity


# Create your views here.


class FilmListView(ListView):
    model = Film
    template_name = 'pages/film_list.html'
    context_object_name = 'films'
    queryset = Film.objects.all().order_by('-release')


class FilmDetailView(DetailView):
    model = Film
    template_name = 'pages/film_details.html'
    context_object_name = 'film'
    queryset = Film.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actors'] = Celebrity.objects.filter(role__name="Актер")
        context['directors'] = Celebrity.objects.filter(role__name="Режиссер")

        return context









