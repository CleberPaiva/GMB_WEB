from django.urls import path
from .views import PessoaCreate
from . import views


urlpatterns = [
    path('editar/<int:pk>/', views.pessoa_edit, name='pessoa_edit'),
    path('list/', views.pessoa_list, name='pessoa_list'),
    path('novo/', PessoaCreate.as_view(), name='pessoa_create'),
]
