from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

# Register your models here.

@admin.register(User)
class LogUser_admin(admin.ModelAdmin):
    list_display = [
        'username',
        'email',
        'avatar',
        'birth_date',
        'city',
        'gender',
        'about',


    ]
