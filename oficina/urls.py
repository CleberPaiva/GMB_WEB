from django.urls import path
from .views import OficinaCreate
from . import views


urlpatterns = [
    path('editar/<int:pk>/', views.oficina_edit, name='oficina_edit'),
    path('list/', views.oficina_list, name='oficina_list'),
    path('novo/', OficinaCreate.as_view(), name='oficina_create'),
    path('tabela/', views.oficina_tabela, name='oficina_tabela'),
]
