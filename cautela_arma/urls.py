from django.urls import path, include
from .views import CautelaCreate
from . import views


urlpatterns = [
    path("", include('core.urls')),
    path('novo/', views.cautela_nova, name='cautela_nova'),
    path('editar/<int:pk>/', views.cautela_edit, name='cautela_edit'),
    path('list/', views.cautela_list, name='cautela_list'),
    path('cautela/<int:pk>/', views.cautela_arma, name='cautela_arma'),
    path('servidor/', views.servidor, name='servidor'),
    path('arma/', views.arma, name='arma'),    
]
