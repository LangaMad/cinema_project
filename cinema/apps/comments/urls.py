from django.urls import path
from .views import *


urlpatterns = [
    path('comment/', (), name='comment'),
    path('/', (), name=''),
    path('/', (), name=''),
]