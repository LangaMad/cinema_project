from django.urls import path
from .views import *
from django.urls import path, include

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]