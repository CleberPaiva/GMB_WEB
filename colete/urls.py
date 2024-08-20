from django.urls import path, include
from .views import ColeteCreate
from . import views


urlpatterns = [
    path("", include('core.urls')),
    path('editar/<int:pk>/', views.colete_edit, name='colete_edit'),
    path('list/', views.colete_list, name='colete_list'),
    path('novo/', ColeteCreate.as_view(), name='colete_create'),
    path('tabela/', views.colete_tabela, name='colete_tabela'),
    path('cautela/<int:pk>/', views.colete_cautela, name='colete_cautela'),
    path('cautela_imprime/<int:pk>/', views.colete_cautela_imprime, name='colete_cautela_imprime'),
    path('devolucao/<int:pk>/', views.colete_devolucao, name='colete_devolucao'),
    path('add_colete/', views.add_colete, name='add_colete'),
    path('edit_colete/<int:pk>/', views.edit_colete, name='edit_colete'),
    path('get_colete_details/', views.get_colete_details, name='get_colete_details'),
]
