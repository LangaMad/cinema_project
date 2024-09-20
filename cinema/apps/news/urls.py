from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.category_list, name='category_list'),
    path('tag/', views.tag_list, name='tag_list'),
    path('post/', views.post_list, name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
]



