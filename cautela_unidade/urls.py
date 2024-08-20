from django.urls import path, include
from . import views

urlpatterns = [
    path("", include('core.urls')),
    path('list/', views.unidade_list, name='unidade_list'),
    path('unidade/<int:pk>/', views.unidade, name='unidade'),
    path('unidade_imprimir/<int:pk>/', views.unidade_imprimir, name='unidade_imprimir'),
]
