"""Home URLS"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('privacy/', views.privacy, name='privacy'),
    path('404/', views.handler404, name='404'),
]
