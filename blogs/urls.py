from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('posts-list', views.PostsView.as_view(), name='posts-list'),


]
