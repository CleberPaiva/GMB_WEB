from django.urls import path
from .views import home
from .views import cadastros, fabricantes, estoque, municoes


urlpatterns = [
    path('', home, name='home'),
    path('cadastros/', cadastros, name='cadastros'),
    path('fabricantes/', fabricantes, name='fabricantes'),
    path('estoque/', estoque, name='estoque'),
    path('municoes/', municoes, name='municoes'),
]
