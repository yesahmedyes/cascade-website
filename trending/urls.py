from django.urls import path
from . import views


app_name = 'trending'


urlpatterns = [
    path('', views.trending_page, name='trending'),
]