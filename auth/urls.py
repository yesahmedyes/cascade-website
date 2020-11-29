from django.urls import path
from . import views


app_name = 'auth'

# these are some of our urls in a python file called urls.py

urlpatterns = [
    path('login', views.login_page, name='login'),
    path('signup', views.signup, name='signup'),
    path('register', views.register, name='register'),
    path('logout', views.logout_page, name='logout')
]