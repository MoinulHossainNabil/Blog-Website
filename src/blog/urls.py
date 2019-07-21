
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from posts.views import blog, index, post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',blog, name = 'blog_details'),
    path('index/',index),
    path('post/<id>/',post, name = 'post_details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
