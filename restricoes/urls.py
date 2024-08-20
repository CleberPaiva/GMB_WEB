from django.urls import path, include
from .views import RestricoesCreate
from . import views


urlpatterns = [
    path("", include('core.urls')),
    path('restricoes/', views.restricoes_index, name='restricoes_index'),
    path('editar/<int:pk>/', views.restricoes_edit, name='restricoes_edit'),
    path('list/', views.restricoes_list, name='restricoes_list'),
    path('novo/', RestricoesCreate.as_view(), name='restricoes_create'),
    path('tabela/', views.restricoes_tabela, name='restricoes_tabela'),
    path('cautela/<int:pk>/', views.restricoes_cautela, name='restricoes_cautela'),
    path('restricoes_cautela_imprime/<int:pk>/', views.restricoes_cautela_imprime, name='restricoes_cautela_imprime'),
    path('devolucao/<int:pk>/', views.restricoes_devolucao, name='restricoes_devolucao'),
    path('aula/', views.restricoes_aula, name='restricoes_aula'),
]
