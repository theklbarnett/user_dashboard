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
    path('users/new', views.render_add_user),
    path('users/edit/', views.render_edit_profile),
    path('users/edit/<int:id>', views.render_edit_user),
    path('users/edit/update_password', views.update_password),
    path('users/edit/<int:id>/update_password', views.update_password),
    path('users/edit/update_description', views.update_description),
    path('users/edit/<int:id>/update_description', views.update_description),
    path('users/edit/update_info', views.update_info),
    path('users/edit/<int:id>/update_info', views.update_info),
    path('users/remove/<int:id>', views.remove_user),
]