from django.urls import path
from . import views


app_name = 'user'


urlpatterns = [
    path('', views.my_profile, name='profile'),
    path('<slug>/', views.my_profile, name='profile'),
    path('follow', views.follow_person, name='follow'),
    path('followers', views.get_followers, name='followers'),
]