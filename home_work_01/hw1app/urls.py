from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('games/', views.games, name='games'),
    path('cube/', views.cube, name='cube'),
    path('heads_or_tails/', views.heads_or_tails, name='heads_or_tails'),
    path('random_number/', views.random_number, name='random_number'),
]
