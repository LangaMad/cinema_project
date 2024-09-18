from django.db import models

from cinema_project.cinema.apps import film


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


class Like(models.Model):
    film_comment = models.ManyToManyField(FilmComments, on_delete = models.CASCADE, related_name = 'likes')
    user = models.ForeignKey('accounts.User', on_delete = models.CASCADE)
    like = models.PositiveIntegerField('likes')
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'



