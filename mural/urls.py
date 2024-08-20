from django.urls import path
from .views import MuralCreate
from . import views


urlpatterns = [
    path('list/', views.mural_list, name='mural_list'),
    path('mural/', MuralCreate.as_view(), name='create_mural'),
]
