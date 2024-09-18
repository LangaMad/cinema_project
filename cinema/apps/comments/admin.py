from django.contrib import admin

from cinema.apps.comments.models import Post_Comment


# Register your models here.
@admin.register(Post_Comment)
class PostComment(admin.ModelAdmin):
    list_display = [
        'post',
        'author',
        'text',
        'created_at',
        'updated_at'
    ]