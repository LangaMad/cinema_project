from django.core.paginator import Paginator
from django.shortcuts import render
from lib2to3.fixes.fix_input import context
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Celebrity
from django.db.models import Q


# Create your views here.

class CelebrityListView(ListView):
    model = Celebrity
    template_name = 'pages/celebrity_list.html'
    context_object_name = 'celebrities'
    queryset = Celebrity.objects.all() # одно и тож
    paginate_by = 2

    def get_queryset(self): #Поисковик
        search_text = self.request.GET.get('query')
        if search_text is None:
            return Celebrity.objects.all()
        q = self.model.objects.filter(
            Q(first_name__icontains = search_text) | # and - |
            Q(surname__icontains=search_text) |
            Q(country__icontains=search_text) |
            Q(role__icontains=search_text)
        )
        return q

    # def get_queryset(self): #Поисковик
    #     search_text = self.request.GET.get('query')
    #     if search_text is None:
    #         return Celebrity.objects.all()
    #     q = self.model.objects.filter(
    #         Q(title__icontains = search_text) | # and - |
    #         Q(text__icontains=search_text) |
    #         Q(text2__icontains=search_text) |
    #         Q(text3__icontains=search_text)
    #     )
    #     return q






class CelebrityDetailView(DetailView):
    model = Celebrity
    template_name = 'pages/celebrity.html'
    context_object_name = 'celebrity'
    queryset = Celebrity.objects.all()
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['previous_celebrity'] = Celebrity.objects.filter(id__lt=self.object.id).order_by('-id').first()
        context['next_celebrity'] = Celebrity.objects.filter(id__gt=self.object.id).order_by('id').first()
        return context


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
#         queryset = Ce.objects.filter(category__slug = self.kwargs['slug'])
#
#         search_text = self.request.GET.get('query')
#         if search_text is None:
#             return Celebrity.objects.all()
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
    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context['category_post'] = Celebrity.objects.filter(
        #      slug = self.kwargs['slug']
        # )
        # context['form'] = SearchForm()
        #  context['categories'] = Celebrity.objects.all()
        #     return context

