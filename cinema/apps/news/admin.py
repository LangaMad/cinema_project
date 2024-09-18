from django.contrib import admin

from .models import *


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
        'text',
        'created_at',
        'updated_at',
        'is_active',
        'main_image'

    ]
    filter_horizontal = ('tags',)

@admin.register(Post_Image)
class PostImage(admin.ModelAdmin):
    list_display = [
        'image1',
        'image2',
        'image3',
        'image4'
        ]

