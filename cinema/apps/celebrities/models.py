from django.db import models

# Create your models here.
class Celebrity(models.Model):
    first_name = models.CharField('Имя', max_length=100, blank = True, null = True)
    surname = models.CharField('Фамилия',max_length=100, blank = True, null = True)
    birth_date = models.DateTimeField('Дата рождения', blank = True, null = True)
    biography = models.TextField('Биография', blank = True, null = True)
    country = models.CharField('Страна', max_length=100, blank = True, null = True)
    image = models.ImageField('Изображение1', upload_to='post_images/',
                              blank=True, null=True)
    is_alive = models.BooleanField('Жив', blank = True, null = True)
    short_bio = models.TextField('Биография кратко', blank = True, null = True)


