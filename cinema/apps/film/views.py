
from django.views.generic import ListView, DetailView

from .models import *
from django.shortcuts import render
from .forms import FilmCommentsForm
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
    # paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actors'] = Celebrity.objects.filter(role__name="Актер")
        context['directors'] = Celebrity.objects.filter(role__name="Режиссер")
        context['screenwriter'] = Celebrity.objects.filter(role__name="Сценарист")
        context['producer'] = Celebrity.objects.filter(role__name="Продюссер")
        context['trailer'] = Trailer.objects.filter(film=self.object)
        context['frames'] = FilmFrame.objects.filter(film=self.object)
        context['previous_film'] = Film.objects.filter(id__lt=self.object.id).order_by('-id').first()
        context['next_film'] = Film.objects.filter(id__gt=self.object.id).order_by('id').first()
        context['form'] = FilmCommentsForm()
        return context









