from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="index"),
    path('general/', general, name="general"),
    path('video_juegos/', videojuegos, name="videojuegos"),
    path('programacion/', programacion, name="programacion"),
    path('ciencia_ficcion/', cienciaficcion, name="cienciaficcion"),
    path('tecnologia/', tecnologia, name="tecnologia"),
]
