from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Category, Tag, Post

class PostListView(ListView):
    model = Post
    template_name = 'pages/news_list.html'
    context_object_name = 'news'
    queryset = Post.objects.all().order_by('-created_at')
    paginate_by = 2

class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/news_details.html'
    context_object_name = 'post'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['last_post'] = Post.objects.all()[:3]
        return context















