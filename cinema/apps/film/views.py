from django.db.models import Q

from django.views.generic import ListView, DetailView,View

from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from .forms import FilmCommentsForm, SearchForm, RatingForm
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

    def get_queryset(self):
        search_text = self.request.GET.get('query')
        if search_text is None:
            return Film.objects.all()
        q = self.queryset.filter(
            Q(name__icontains=search_text) |
            Q(origin_name__icontains=search_text)
        )
        return q

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forma'] = SearchForm(self.request.GET)
        return context


class FilmDetailView(DetailView):
    model = Film
    template_name = 'pages/film_details.html'
    context_object_name = 'film'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()
        context['actors'] = Celebrity.objects.filter(role__name="Актер")
        context['directors'] = Celebrity.objects.filter(role__name="Режиссер")
        context['screenwriter'] = Celebrity.objects.filter(role__name="Сценарист")
        context['producer'] = Celebrity.objects.filter(role__name="Продюссер")
        context['trailer'] = Trailer.objects.filter(film=self.object)
        context['frames'] = FilmFrame.objects.filter(film=self.object)
        context['previous_film'] = Film.objects.filter(id__lt=self.object.id).order_by('-id').first()
        context['next_film'] = Film.objects.filter(id__gt=self.object.id).order_by('id').first()
        context['comments'] = FilmComments.objects.filter(post=film)
        context['form'] = FilmCommentsForm()
        context['rating_form'] = RatingForm()
        context['forma'] = SearchForm(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        film = self.get_object()
        comment_form = FilmCommentsForm(request.POST)
        rating_form = RatingForm(request.POST)

        if 'submit_comment' in request.POST and comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = film
            comment.author = request.user
            comment.save()
            return redirect('film_details', pk=film.pk)


        elif 'submit_rating' in request.POST and rating_form.is_valid():
            rating = int(rating_form.cleaned_data['rating'])
            film.update_average_rating(rating)
            return redirect('film_details', pk=film.pk)


        context = self.get_context_data(comment_form=comment_form, rating_form=rating_form)
        return self.render_to_response(context)

    def get_queryset(self):
        search_text = self.request.GET.get('query')
        if search_text is None:
            return Film.objects.all()
        q = self.queryset.filter(
            Q(name__icontains=search_text) |
            Q(origin_name__icontains=search_text)
        )
        return q


class AddToFavoritesView(View):
    def post(self, request, *args, **kwargs):
        film_id = request.POST.get('film_id')  # Получаем ID фильма из POST-запроса
        film = get_object_or_404(Film, id=film_id)  # Находим фильм по ID

        if request.user.is_authenticated:
            request.user.fav_movies.add(film)  # Добавляем фильм в избранное
            return redirect('user_page')  # Перенаправление на страницу профиля

        return redirect('signin')






