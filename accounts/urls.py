from django.urls import path
from .views import register, log_in, home


urlpatterns = [
    path('signup/', register, name='signup'),
    path('login', log_in, name='login'),
    path('home', home, name='home'),
]