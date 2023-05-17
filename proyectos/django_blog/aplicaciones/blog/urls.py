from django.contrib import admin
from django.urls import path
from .views import home, general

urlpatterns = [
    path('', home, name="index"),
    path('general/', general, name="general")
]