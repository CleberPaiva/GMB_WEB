from django.urls import path
from .views import UnidadeCreate
from . import views


urlpatterns = [
    path('novo', UnidadeCreate.as_view(), name='create_unidade'),
    path('editar/<int:pk>/', views.edit_unidade, name='edit_unidade'),
    path('list/', views.unidade_list, name='unidade_list'),
]
