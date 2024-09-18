from django.contrib import admin

from cinema.apps.celebrities.models import Celebrity


# Register your models here.
@admin.register(Celebrity)
class PostImage(admin.ModelAdmin):
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