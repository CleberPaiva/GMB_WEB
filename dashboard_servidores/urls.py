from django.urls import path
from . import views

urlpatterns = [
    path('ver/', views.dashboard_with_pivot_servidores, name='dashboard_with_pivot_servidores'),
    path('data_servidores', views.pivot_data_servidores, name='pivot_data_servidores'),
]