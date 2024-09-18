from django.urls import path
from .views import *


urlpatterns = [
    path('', (), name='home'),
    path('about_us/', (), name='about_us'),
    path('vacancy/', (), name='vacancy'),
    path('vacancy_answer/', (), name='vacancy_answer'),
    path('argeement/', (), name='argeement'),
]