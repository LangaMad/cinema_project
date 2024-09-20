from django.urls import path
from .views import *
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(), name='signin'),
    path('logout/', logout1, name='logout'),

]