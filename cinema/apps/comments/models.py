from django.db import models

from cinema.apps.news.models import Post


# Create your models here.

class Post_Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comments')
    author = models.ForeignKey('accounts.User', on_delete = models.CASCADE)
    text = models.TextField('Текст')
    created_at = models.DateTimeField('Дата создания', auto_now_add = True)
    updated_at = models.DateTimeField('Дата обновдения', auto_now =True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'