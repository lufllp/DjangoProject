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
    path('author', views.author_list, name='author_list'),
    path('author/new/', views.author_create, name='author_create'),
    path('author/edit/<int:pk>/', views.author_update, name='author_update'),
    path('author/delete/<int:pk>/', views.author_delete, name='author_delete'),
]
