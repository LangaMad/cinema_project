from django.contrib import admin

from .models import PostComment


# Register your models here.
@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = [
        'post',
        'author',
        'text',
        'created_at',
        'updated_at'
    ]