from django.urls import path
from .views import *


urlpatterns = [
    path('signup/', (), name='signup'),
    path('signin/', (), name='signin'),
    path('logout/', (), name='logout'),
]