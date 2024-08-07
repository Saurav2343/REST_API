from django.urls import path
from . import views

urlpatterns=[
    path('', views.getData, name = 'GetItems'),
    path('add/', views.addItem, name='AddItems'),
    path('delete/<int:pk>/', views.deleteItem, name='DeleteItem'),
]