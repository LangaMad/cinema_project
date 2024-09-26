from django.contrib import admin
from django.contrib.auth.models import User
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
        #'fav_movies'

    ]
    filter_horizontal = ['fav_movies']
