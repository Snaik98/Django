# from django.contrib import admin
from django.urls import path
from FIRSTAPPLICATION import views

urlpatterns = [
    path('', views.index),
    path('index', views.index1)
]