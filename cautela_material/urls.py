from django.urls import path, include
from .views import add_cautela
from . import views


urlpatterns = [
    path("", include('core.urls')),
    path('add_cautela/', views.add_cautela, name='add_cautela'),  
    path('ajax/material_info/', views.material_info, name='material_info'), 
]
