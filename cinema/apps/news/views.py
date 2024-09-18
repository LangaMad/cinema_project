# from lib2to3.fixes.fix_input import context
#
# from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView
# from .models import Post, Category, Post_Comment, Post_Image
# from django.db.models import Q
#
#
# # Create your views here.
#
# class PostListView(ListView):
#     model = Post
#     template_name = 'pages/post_list.html'
#     context_object_name = 'posts'
#     queryset = Post.objects.all().order_by('-created_at') # одно и тоже
#     paginate_by = 2
#
#     def get_queryset(self): #Поисковик
#         search_text = self.request.GET.get('query')
#         if search_text is None:
#             return Post.objects.all()
#         q = self.model.objects.filter(
#             Q(title__icontains = search_text) | # and - |
#             Q(text__icontains=search_text) |
#             Q(text2__icontains=search_text) |
#             Q(text3__icontains=search_text)
#         )
#         return q
#
#
#
#             # return Post.objects.filter(title__incontains = search_text)
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all() # одно и тоже
#         context['last_post'] = Post.objects.all()[:3]
#         context['form'] = SearchForm(self.request.GET)
#         return context
#
#
# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'pages/post_detail.html'
#     context_object_name = 'post'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all() # одно и тоже
#         context['last_post'] = Post.objects.all()[:3]
#         context['form'] = CommentForm()
#         context['comments'] = Comment.objects.filter(post = self.object)
#         return context
#
#     def post(self, request, *args, **kwargs):
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit = False)
#             comment.post = self.get_object()
#             comment.author = request.user
#             comment.save()
#             return redirect('post_detail', pk = self.get_object().pk)
#         return self.render_to_response(self.get_context_data(form = form))
#
# class CategoryListView(ListView):
#     model = Post
#     template_name = 'pages/category_list.html'
#     context_object_name = 'pos_category'
#     paginate_by = 2
#
#     def get_queryset(self): #Поисковик
#         queryset = Post.objects.filter(category__slug = self.kwargs['slug'])
#
#         search_text = self.request.GET.get('query')
#         if search_text is None:
#             return Post.objects.all()
#         queryset = queryset.filter(
#             Q(title__icontains = search_text) | # and - |
#             Q(text__icontains=search_text) |
#             Q(text2__icontains=search_text) |
#             Q(text3__icontains=search_text)
#         )
#         return queryset
#
#     # def get_queryset(self):
#     #     return Post.objects.filter(category__slug = self.kwargs['slug'])
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category_post'] = Category.objects.filter(
#             slug = self.kwargs['slug']
#         )
#         context['form'] = SearchForm()
#         context['categories'] = Category.objects.all()
#         return context
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
