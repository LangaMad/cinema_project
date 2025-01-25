from django.urls import path
from .views import *

urlpatterns = [
    path('news_list/', PostListView.as_view(), name='news_list'),
    path('news_details/<int:pk>/', PostDetailView.as_view(), name='news_details'),
]



