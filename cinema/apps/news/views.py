from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .forms import PostCommentsForm
from ..film.forms import SearchForm
from .models import Category, Tag, Post
from ..comments.models import PostComment
from django.db.models import Q

class PostListView(ListView):
    model = Post
    template_name = 'pages/news_list.html'
    context_object_name = 'news'
    queryset = Post.objects.all().order_by('-created_at')
    paginate_by = 3

    def get_queryset(self):
        search_text = self.request.GET.get('query')
        if search_text is None:
            return Post.objects.all()
        q = self.queryset.filter(
            Q(title__icontains=search_text) |
            Q(text__icontains=search_text)
        )
        return q

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forms'] = SearchForm(self.request.GET)
        return context

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

    # def get_queryset(self):
    #     search_text = self.request.GET.get('query')
    #     if search_text is None:
    #         return Post.objects.all()
    #     q = self.queryset.filter(
    #         Q(name__icontains=search_text) |
    #         Q(origin_name__icontains=search_text)
    #     )
    #     return q













