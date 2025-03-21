from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('autre', views.other_page, name='other_page'),
    path('create/', views.product_create, name='product_create'),
    path('update/<int:pk>/', views.product_update, name='product_update'),
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),
]