from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('post/', views.post, name='post'),
    re_path(r'(?P<article_url>[\w-]+)/$', views.post, name='post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)