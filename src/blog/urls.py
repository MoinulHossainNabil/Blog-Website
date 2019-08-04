
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from posts.views import blog, index, post, search_for_post, post_create, post_delete, post_update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',blog, name = 'blog_details'),
    path('index/',index),
    path('post/<id>/',post, name = 'post_details'),
    path('create/',post_create, name = 'post_create'),
    path('post/<id>/update/',post_update, name = 'post_update'),
    path('post/<id>/delete/',post_delete, name = 'post_delete'),
    path('search_for_post/', search_for_post, name = 'search_for_post'),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
