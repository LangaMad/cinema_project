from django.contrib import admin

from .models import PostComment
from .models import PostComment, FilmComments, LikeFilmComments


# Register your models here.
@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = [
        'post',
        'author',
        'text',
        'created_at',
        'updated_at'
    ]

@admin.register(FilmComments)
class FilmCommentsAdmin(admin.ModelAdmin):
    list_display = [
        'post',
        'author',
        'text',
        'created_at',
        'updated_at'
    ]
    filter_horizontal = ('like',)