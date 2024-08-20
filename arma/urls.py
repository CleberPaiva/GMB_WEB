from django.urls import path, include
from .views import ArmaCreate
from . import views


urlpatterns = [
    path("", include('core.urls')),
    path('editar/<int:pk>/', views.arma_edit, name='arma_edit'),
    path('list/', views.arma_list, name='arma_list'),
    path('novo/', ArmaCreate.as_view(), name='arma_create'),
    path('tabela/', views.arma_tabela, name='arma_tabela'),
    path('cautela/<int:pk>/', views.arma_cautela, name='arma_cautela'),
    path('cautela_imprime/<int:pk>/', views.arma_cautela_imprime, name='arma_cautela_imprime'),
    path('devolucao/<int:pk>/', views.arma_devolucao, name='arma_devolucao'),
    path('add_arma/', views.add_arma, name='add_arma'),
    path('edit_arma/<int:pk>/', views.edit_arma, name='edit_arma'),
    path('get_arma_details/', views.get_arma_details, name='get_arma_details'),
]