from django.urls import path, include
from .views import adicionar_cautela, add_cautela_material_total
from . import views


urlpatterns = [
    path("", include('core.urls')),
    path('add_cautela_total/', views.add_cautela_material_total, name='add_cautela_material_total'),
    path('adicionar_cautela/', views.adicionar_cautela, name='adicionar_cautela'),  
    path('ajax/material_info/', views.material_info, name='material_info'), 
    path('lista/', views.lista_material_cautela, name='lista_material_cautela'),
    path('exibe/<int:pk>/', views.exibe_cautela, name='exibe_cautela'),    
    path('add_material_total/', views.add_material_total_form, name='add_material_total'),
    path('save_material_total/', views.add_material_total_save, name='save_material_total'),
    path('add_material/<int:pk>/', views.add_material, name='add_material'),
    path('ajax/material_detail/', views.material_detail, name='material_detail'),
    path('imprime/<int:pk>/', views.cautela_material_imprime, name='cautela_material_imprime'),
]
