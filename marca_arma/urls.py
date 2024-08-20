from django.urls import path
from .views import MarcaArmaCreate
from . import views


urlpatterns = [
    path('editar/<int:pk>/', views.marca_arma_edit, name='marca_arma_edit'),
    path('list/', views.marca_arma_list, name='marca_arma_list'),
    path('novo/', MarcaArmaCreate.as_view(), name='marca_arma_create'),
    path('tabela/', views.marca_arma_tabela, name='marca_arma_tabela'),
]
