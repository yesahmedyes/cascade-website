from django.urls import path
from . import views


app_name = 'posts'


urlpatterns = [
    path('update_post', views.update_post, name='update_post'),
    path('fetch_comments', views.fetch_comments, name='fetch_comments')
]