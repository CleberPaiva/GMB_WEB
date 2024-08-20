from django.urls import path
from .views import MaterialCreate
from . import views


urlpatterns = [
    path('editar/<int:pk>/', views.material_edit, name='material_edit'),
    path('list/', views.material_list, name='material_list'),
    path('novo/', MaterialCreate.as_view(), name='material_create'),
    path('tabela/', views.material_tabela, name='material_tabela'),
    path('tabelaprojetil/', views.projetil_tabela, name='projetil_tabela'),
]
