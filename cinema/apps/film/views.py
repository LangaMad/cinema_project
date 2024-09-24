from django.db.models import Q

from django.views.generic import ListView, DetailView,View

from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from .forms import FilmCommentsForm
from ..celebrities.models import Celebrity
from ..accounts.models import User
from ..comments.models import FilmComments


# Create your views here.


class FilmListView(ListView):
    model = Film
    template_name = 'pages/film_list.html'
    context_object_name = 'films'
    queryset = Film.objects.all().order_by('-release')
    paginate_by = 2


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
        context['comments'] = FilmComments.objects.filter(post=self.object)
        return context


    def post(self, request, *args, **kwargs):
        form = FilmCommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.get_object()
            comment.author = request.user
            comment.save()
            return redirect('film_details', pk=self.get_object().pk)
        return self.render_to_response(self.get_context_data(form=form))


class AddToFavoritesView(View):
    def post(self, request, *args, **kwargs):
        film_id = request.POST.get('film_id')  # Получаем ID фильма из POST-запроса
        film = get_object_or_404(Film, id=film_id)  # Находим фильм по ID

        if request.user.is_authenticated:
            request.user.fav_movies.add(film)  # Добавляем фильм в избранное
            return redirect('user_page')  # Перенаправление на страницу профиля

        return redirect('signin')







