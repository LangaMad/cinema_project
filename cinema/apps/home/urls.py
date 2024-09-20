from django.urls import path
from .views import *
from django.urls import path, include

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about_us/', AboutUsView.as_view(), name='about_us'),
    path('agreement/', AgreementView.as_view(), name='agreement'),
    path('vacancy_list/', VacancyListView.as_view(), name='vacancy_list'),
    path('vacancy_detail/<int:pk>/', VacancyDetailView.as_view(), name='vacancy_detail')
]
