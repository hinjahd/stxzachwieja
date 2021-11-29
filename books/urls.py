from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('create', views.createBook, name="create"),
    path('update/<str:pk>/', views.updateBook, name="update"),
    path('delete/<str:pk>/', views.deleteBook, name="delete"),
    path('search', views.search, name="search"),
]