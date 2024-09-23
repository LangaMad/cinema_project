from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(User)
class Register_admin(admin.ModelAdmin):
    list_display = [
        'username',
        'email',
        'avatar',
        'birth_date',
        'city',
        'gender',
        'about',

    ]
    filter_horizontal = ('fav_movies',)
