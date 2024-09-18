from django.contrib import admin
from django.contrib.auth.models import User


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
        'fav_movies'

    ]
