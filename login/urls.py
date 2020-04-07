from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signin', views.render_signin), 
    path('register', views.render_register), 
    path('', views.render_home), 
]