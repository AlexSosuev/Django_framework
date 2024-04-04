from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about_me/', views.about_me, name='about_me'),
    path('create_client/', views.create_client, name='create_client'),
    path('upd_client/', views.update_client, name='update_client'),
    path('del_client/', views.delete_client, name='delete_client'),
    path('orders/', views.orders_list, name='order_list'),
    path('ordered-products/<str:period>/', views.orders_list_time, name='ordered_products_list'),
]