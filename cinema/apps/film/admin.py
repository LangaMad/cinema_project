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


@admin.register(Film)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'origin_name',
        'image',
        'release',
        'country',
        'slogan',
        'director',
        'screenwriter',
        'producer',
        'operator',
        'composer',
        'artist',
        'installation',
        'actors',
        'dubbing_actors',
        'budget',
        'time',
        'trailer',
        'trailer2'

    ]
    filter_horizontal = ('genre',)




