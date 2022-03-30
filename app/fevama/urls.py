from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from fevama import views

app_name = 'fevama'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('password/', auth_views.PasswordChangeView.as_view(template_name="fevama/change-password.html"), name="password")
]