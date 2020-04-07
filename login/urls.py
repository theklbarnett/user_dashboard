from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_home), 
    path('signin', views.render_signin), 
    path('register', views.render_register), 
    path('dashboard', views.render_user_dashboard),
    path('ajax/email_uniqueness', views.email_uniqueness),
    path('register_user', views.register_user),
    path('authenticate', views.authenticate_user),
    path('logout', views.logout),
]