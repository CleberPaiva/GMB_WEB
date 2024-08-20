from django.urls import path
from . import views

urlpatterns = [
    path('ver/', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('data', views.pivot_data, name='pivot_data'),
]