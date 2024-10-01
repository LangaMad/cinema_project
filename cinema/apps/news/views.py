from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from .models import Category, Tag, Post
from ..comments.models import PostComment
from .forms import *

class PostListView(ListView):
    model = Post
    template_name = 'pages/news_list.html'
    context_object_name = 'news'
    queryset = Post.objects.all().order_by('-created_at')
    paginate_by = 2

class NewsDetailView(DetailView):
    model = Post
    template_name = 'pages/news_details.html'
    context_object_name = 'post'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comment'] = PostComment.objects.filter(post=post)
        context['form1'] = PostCommentsForm()
        return context

    def post(self, request, *args, **kwargs):
        form = PostCommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.get_object()
            comment.author = request.user
            comment.save()
            return redirect('news_details', pk=self.get_object().pk)
        return self.render_to_response(self.get_context_data(form=form))















