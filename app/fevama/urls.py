from django.contrib import admin
from django.urls import path, include

from fevama import views

app_name = 'fevama'
urlpatterns = [
    path('home/', views.home, name='home'),
]