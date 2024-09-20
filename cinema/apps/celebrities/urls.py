from django.urls import path
from .views import *


urlpatterns = [
    path('celebrity_list/', CelebrityListView.as_view(), name = 'celebrity_list' ),
    path('celebrity_detail/', CelebrityDetailView.as_view(), name = 'celebrity_detail'),
]