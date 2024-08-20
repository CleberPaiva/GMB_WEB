from django.urls import path
from .views import MarcaMunicaoCreate
from . import views


urlpatterns = [
    path('editar/<int:pk>/', views.marca_municao_edit, name='marca_municao_edit'),
    path('list/', views.marca_municao_list, name='marca_municao_list'),
    path('novo/', MarcaMunicaoCreate.as_view(), name='marca_municao_create'),
    path('tabela/', views.marca_municao_tabela, name='marca_municao_tabela'),
]
