from django.urls import path
from .views import MarcaEpiCreate
from . import views


urlpatterns = [
    path('editar/<int:pk>/', views.marca_epi_edit, name='marca_epi_edit'),
    path('list/', views.marca_epi_list, name='marca_epi_list'),
    path('novo/', MarcaEpiCreate.as_view(), name='marca_epi_create'),
    path('tabela/', views.marca_epi_tabela, name='marca_epi_tabela'),
]
