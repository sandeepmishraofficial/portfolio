from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # PWA: Serve Service Worker from root so it can control the full origin
    path('serviceworker.js', views.service_worker, name='service_worker'),
]
