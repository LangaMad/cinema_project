from django.urls import path
from .views import *


urlpatterns = [
    path('film/', (), name='film'),


]