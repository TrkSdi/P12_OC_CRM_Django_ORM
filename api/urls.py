from django.contrib import admin
from django.urls import path, include
from .views import getUser


urlpatterns = [
    path('users/', getUser )
]