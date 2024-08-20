from django.urls import path, include
from .views import MunicaoCreate
from . import views


urlpatterns = [
    path("", include('core.urls')),
    path('list/', views.municao_list, name='municao_list'),
    path('novo/', MunicaoCreate.as_view(), name='add_municao'),
    path('imprime/<int:pk>/', views.municao_imprime, name='municao_imprime'),
]