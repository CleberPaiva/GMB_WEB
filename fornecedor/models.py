from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Fornecedor(models.Model):
    nomefantasia = models.CharField(max_length=80, verbose_name='NOME FANTASIA')
    razaosocial = models.CharField(max_length=80, verbose_name='RAZÃO SOCIAL')
    endereco = models.CharField(max_length=100, verbose_name='ENDEREÇO')
    telefone = models.CharField(max_length=50, verbose_name='TELEFONE')
    email = models.CharField(max_length=80, verbose_name='email')


    def __str__(self):
        return self.nomefantasia

    def get_absolute_url(self):
        return reverse('fornecedor_list')
