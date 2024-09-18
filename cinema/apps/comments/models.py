from django.db import models



class FilmComments(models.Model):
    post = models.ForeignKey('film.Film' ,on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    text = models.TextField('Текст')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return  self.text

    class Meta:
        verbose_name ='Комментарий'
        verbose_name_plural = 'Комментарии'


class LikeFilmComments(models.Model):
    film_comment = models.ManyToManyField(FilmComments, related_name='likes')
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    like = models.PositiveIntegerField('likes')
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'



from cinema.apps.news.models import Post


# Create your models here.

class PostComment(models.Model):
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