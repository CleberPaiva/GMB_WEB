from django.urls import path
from .views import MensagemCreate
from . import views


urlpatterns = [
    path('list/', views.mensagem_list, name='mensagem_list'),
    path('mural/', MensagemCreate.as_view(), name='create_mensagem'),
]
