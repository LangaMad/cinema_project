
from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Raiting)
class RaitingAdmin(admin.ModelAdmin):
    list_display = ['rait']


class FilmFrameInline(admin.TabularInline):
    model = FilmFrame
    extra = 1


class TrailerInline(admin.TabularInline):
    model = Trailer
    extra = 1


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'origin_name',
        'poster',
        'release',
        'country',
        'slogan',
        'budget',
        'time',
        'average_rating',
        'rating_count'
    ]
    filter_horizontal = ('genre','celebrity',)
    inlines = [FilmFrameInline, TrailerInline]




