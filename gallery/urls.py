from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('images/', views.images, name='images'),
    path('videos/', views.videos, name='videos'),
    path('audio/', views.audio, name='audio'),
]