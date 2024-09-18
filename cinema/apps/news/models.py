from enum import unique

from django.db import models

from cinema.apps.news import admin
from cinema.apps.news.admin import PostImage


# Create your models here.

class Category(models.Model):
    name = models.CharField('Название категории', max_length=100,unique = True)
    slug = models.SlugField('Slug', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    name = models.CharField('Название категории', max_length=100, unique=True)
    slug = models.SlugField('Slug', unique=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name ='Тег'
        verbose_name_plural ='Теги'

class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Текст')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,verbose_name= 'Теги', related_name = 'posts')
    main_image = models.ImageField('Изображение', upload_to='images/',
                              blank=True, null=True)




class PostImage(models.Model):
    post_images = models.ForeignKey(Post, related_name='post_images', on_delete=models.CASCADE)
    image1 = models.ImageField('Изображение1',upload_to='post_images/', verbose_name=("Дополнительное изображение"),
                               blank=True, null=True)



class Like(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'likes')
    user = models.ForeignKey('accounts.User', on_delete = models.CASCADE)
    created_at = models.DateTimeField('Дата создания', auto_now_add = True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'