from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.servidor_list, name='servidor_list'),
    path('servidor/<int:pk>/', views.servidor, name='servidor'),
    path('servidor_imprimir/<int:pk>/', views.servidor_imprimir, name='servidor_imprimir'),
]
