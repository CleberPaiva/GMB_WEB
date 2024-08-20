from django.urls import path
from .views import FornecedorCreate
from . import views


urlpatterns = [
    path('editar/<int:pk>/', views.fornecedor_edit, name='fornecedor_edit'),
    path('list/', views.fornecedor_list, name='fornecedor_list'),
    path('novo/', FornecedorCreate.as_view(), name='fornecedor_create'),
]
