from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('show/<int:id>', views.render_messages_home),
    path('post_message', views.post_message),
    path('post_comment', views.post_comment),
    path('show/ajax/delete_post', views.delete_post)
]