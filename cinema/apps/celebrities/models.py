from django.db import models

# Create your models here.
class Celebrity(models.Model):
    first_name = models.CharField('Имя', max_length=100, auto_now_add = True)
    surname = models.CharField('Фамилия',max_length=100, auto_now_add=True)
    birth_date = models.DateTimeField('Дата рождения', auto_now_add = True)
    biography = models.TextField('Биография', auto_now_add = True)
    country = models.CharField('Страна', max_length=100)
    image = models.ImageField('Изображение1', upload_to='post_images/', verbose_name=("Дополнительное изображение"),
                              blank=True, null=True)
    is_alive = models.BooleanField('Жив', null=True)
    short_bio = models.TextField('Биография кратко', null=True, auto_now_add = True)


