from django.urls import path
from .views import *


urlpatterns = [
    path('post/', (), name='post'),
    path('category_post/', (), name='category_post'),
]