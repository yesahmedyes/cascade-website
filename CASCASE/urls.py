from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('home.urls', namespace="home")),
    path('admin/', admin.site.urls),
    path('profile/', include('user.urls', namespace="user")),
    path('trending/', include('trending.urls', namespace="trending")),
    path('post/', include('posts.urls', namespace="posts")),
    path('auth/', include('auth.urls', namespace="auth")),
]

# remove the below during deployment
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
