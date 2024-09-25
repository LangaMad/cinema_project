from django.urls import path
from .views import *
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(), name='signin'),
    path('logout/', logout1, name='logout'),
    path('user_page/',UserpageView.as_view(), name='user_page'),
    path('user_settings/', UserSettingsView.as_view(), name='user_settings'),
    path('change_password/', CustomPasswordChangeView.as_view(), name='change_password'),

]