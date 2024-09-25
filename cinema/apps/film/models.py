from django.core.validators import FileExtensionValidator, MaxValueValidator
from django.db import models



class Genre(models.Model):
    name = models.CharField('Название жанра',max_length=100, unique=True)
    slug = models.SlugField('Slug', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Raiting(models.Model):
    rait = models.DecimalField(max_digits=3, decimal_places=1, validators=[MaxValueValidator(10)])

    def __str__(self):
        return str(self.rait)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Film(models.Model):
    name = models.CharField('Название фильма', max_length=100)
    origin_name = models.CharField('Оригинальное название', max_length=100)
    poster = models.ImageField('Постер фильма', upload_to='images/',
                              blank=True, null=True)
    film = models.FileField('Фильм', upload_to='videos/', blank=True, null=True)
    film_poster = models.ImageField('Фото фильма', upload_to='film_image/',
                              blank=True, null=True)
    release = models.DateTimeField('Дата релиза')
    country = models.CharField('Страна', max_length=100)
    genre = models.ManyToManyField(Genre, verbose_name='Жанры', related_name='genre_films')
    slogan = models.TextField('Слоган', blank=True, null=True)
    celebrity= models.ManyToManyField('celebrities.Celebrity',verbose_name='Celebrity', related_name='celebrity_films')
    budget = models.DecimalField('Бюджет', max_digits=15, decimal_places=2, blank=True, null=True)
    time = models.CharField('Время')
    raiting = models.ForeignKey(Raiting, verbose_name='Рейтинг', on_delete=models.CASCADE)
    film_description = models.TextField('Описание фильма', blank=True, null=True)


class FilmFrame(models.Model):
    film = models.ForeignKey(Film, related_name='film_frames',verbose_name='Кадр', on_delete=models.CASCADE)
    frame = models.ImageField(upload_to='frames/',null=True,blank=True)

    def __str__(self):
        return self.film.name

    class Meta:
        verbose_name = 'Кадр'
        verbose_name_plural = 'Кадры'


class Trailer(models.Model):
    film = models.ForeignKey(Film, related_name='film_trailer',verbose_name='Кадр', on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/', null=True, blank=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    image = models.ImageField('Фото трейлера', upload_to='trailer_images/')
    url = models.URLField('ссылка на трейлер')

    def __str__(self):
        return self.film.name

    class Meta:
        verbose_name = 'Трейлер'
        verbose_name_plural = 'Трейлеры'

