
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('uploadfile/home.html', views.home),
    path('uploadfile/upload.html', views.upload, name=''),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
