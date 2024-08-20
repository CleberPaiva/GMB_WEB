from django.urls import path, include
from .views import ArmaParticularCreate
from . import views


urlpatterns = [
    path("", include('core.urls')),
    path('list/', views.arma_particular_list, name='arma_particular_list'),
    path('novo/', ArmaParticularCreate.as_view(), name='add_arma_create'),
]