from django.urls import path
from . import views

urlpatterns = [
    path('author', views.author_list, name='author_list'),
    path('author/new/', views.author_create, name='author_create'),
    path('author/edit/<int:pk>/', views.author_update, name='author_update'),
    path('author/delete/<int:pk>/', views.author_delete, name='author_delete'),
]
