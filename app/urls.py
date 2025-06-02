from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('new/', views.item_create, name='item_create'),
    path('edit/<int:pk>/', views.item_update, name='item_update'),
    path('delete/<int:pk>/', views.item_delete, name='item_delete'),

    path('categories/', views.category_list, name='category_list'),
    path('categories/new/', views.category_create, name='category_create'),
    path('categories/edit/<int:pk>/', views.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),

    path('albums/new/', views.album_create, name='album_create'),

    path('publishers/new/', views.publisher_create, name='publisher_create'),
    path('authors/new/', views.author_create, name='author_create'),
    path('albums/delete/<int:pk>/', views.album_delete, name='album_delete'),
]
