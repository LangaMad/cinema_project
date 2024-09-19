from django.urls import path
from .views import *


urlpatterns = [
    path('film_list/', FilmListView.as_view(), name='film_list'),
    path('film_details/<int:pk>/', FilmDetailView.as_view(), name='film_details'),
]