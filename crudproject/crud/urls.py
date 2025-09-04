from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # /crud/
    path('', views.index, name='index'),
    
]
