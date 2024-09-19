from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(Celebrity)
class CelebrityAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'surname',
        'birth_date',
        'biography',
        'country',
        'image',
        'is_alive',
        'short_bio'

        ]
    filter_horizontal = ('role',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
