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


class Trailer(models.Model):
    video = models.FileField(upload_to='videos/',null=True,blank=True,
                    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])

    class Meta:
        verbose_name = 'Трейлер'
        verbose_name_plural = 'Трейлеры'

class Raiting(models.Model):
    rait = models.DecimalField(max_digits=3, decimal_places=1, validators=[MaxValueValidator(10)])

    def __str__(self):
        return self.rait

    class Meta:
        verbose_name = 'Рейтинг'


class Film(models.Model):
    name = models.CharField('Название фильма', max_length=100, unique=True)
    origin_name = models.CharField('Название фильма', max_length=100, unique=True)
    image = models.ImageField('Изображение', upload_to='images/',
                              blank=True, null=True)
    release = models.DateTimeField('Дата релиза')
    country = models.CharField('Страна', max_length=100)
    genre = models.ManyToManyField(Genre, verbose_name='Жанры', related_name='films')
    slogan = models.TextField('Слоган', blank=True, null=True)
    director = models.ManyToManyField('celebrities.Director', on_delete=models.CASCADE)
    screenwriter =models.ManyToManyField('celebrities.Screenwriter', on_delete=models.CASCADE)
    producer = models.ManyToManyField('celebrities.Producer', on_delete=models.CASCADE)
    operator = models.ManyToManyField('celebrities.Operator', on_delete=models.CASCADE)
    composer = models.ManyToManyField('celebrities.Composer', on_delete=models.CASCADE,
                                      blank=True, null=True)
    artist = models.ManyToManyField('celebrities.Artist', on_delete=models.CASCADE)
    installation = models.ManyToManyField('celebrities.Installation', on_delete=models.CASCADE)
    actors = models.ManyToManyField('celebrities.Actors', on_delete=models.CASCADE,)
    dubbing_actors = models.ManyToManyField('celebrities.DubActors', on_delete=models.CASCADE, blank=True, null=True)
    budget = models.CharField('Бюджет', max_digits=15, decimal_places=2, blank=True, null=True)
    time = models.PositiveIntegerField('Время')
    trailer = models.ForeignKey(Trailer, verbose_name='Трейлер', on_delete=models.CASCADE)
    trailer2 = models.ForeignKey(Trailer, verbose_name='Трейлер2', on_delete=models.CASCADE)
    raiting = models.ForeignKey(Raiting, verbose_name='Рейтинг', on_delete=models.CASCADE)








