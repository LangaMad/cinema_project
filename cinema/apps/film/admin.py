from tkinter import Frame

from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Trailer)
class TrailerAdmin(admin.ModelAdmin):
    list_display = ['video']


@admin.register(Raiting)
class RaitingAdmin(admin.ModelAdmin):
    list_display = ['rait']


@admin.register(Film)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'origin_name',
        'image',
        'release',
        'country',
        'slogan',
        'celebrity',
        'budget',
        'time',
        'trailer',
        'trailer2',
        'raiting'

    ]
    filter_horizontal = ('genre',)


@admin.register(FilmFrame)
class FilmFrameAdmin(admin.ModelAdmin):
    list_display = [
        'film',
        'frame'
    ]


