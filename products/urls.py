from . import views

from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)