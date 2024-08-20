from django.urls import path
from .views import relatorio, menu, sr01, sr02, sr03, sr04, sr05, sr06, sr07, sr08

urlpatterns = [
    path('relatorio/', relatorio, name='relatorio'),
    path('menu/', menu, name='menu'),
    path('sr01/', sr01, name='sr01'), 
    path('sr02/', sr02, name='sr02'),    
    path('sr03/', sr03, name='sr03'),
    path('sr04/', sr04, name='sr04'),
    path('sr05/', sr05, name='sr05'),
    path('sr06/', sr06, name='sr06'),
    path('sr07/', sr07, name='sr07'),
    path('sr08/', sr08, name='sr08'),
]
