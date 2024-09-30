from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from requests import get
from django.conf import settings
from django.conf.urls.static import static

from authentification import views
from rest_framework.authtoken import views as drfviews

from rest_framework.routers import DefaultRouter

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
     
    path('flutter-login/', views.flutter_login, name='flutter_login'),  

    path('create-alert/', views.create_alert, name='create_alert'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
