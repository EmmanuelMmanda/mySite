from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('posts/<slug:slug>', views.post_detail, name='post_detail'),
    path('posts/<slug:slug>/comment/', views.comment, name='comment'),
    path('posts/', views.posts, name='posts'),
    path('contact/', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

