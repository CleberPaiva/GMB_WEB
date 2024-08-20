from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from unidade.models import Unidade


class Oficina(models.Model):
    dataentrada = models.DateField(blank=True, null=True, verbose_name='DATA DE ENTRADA')
    datasaida = models.DateField(blank=True, null=True, verbose_name='DATA DE SAÍDA')
    numeroseria = models.CharField(max_length=50, verbose_name='NUMERO DE SÉRIE')
    especie = models.CharField(max_length=100, verbose_name='ESPÉCIE')
    modelo = models.CharField(max_length=100, verbose_name='MODELO')
    cargapara = models.CharField(max_length=100, verbose_name='CARGA PARA')
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT)
    historico = models.CharField(max_length=500, verbose_name='HISTÓRICO')
    servico = models.CharField(blank=True, null=True, max_length=500, verbose_name='SERVIÇO')
    usuario = models.CharField(blank=True, max_length=30, verbose_name='USUÁRIO', null=True)
    armeiro = models.CharField(blank=True, max_length=100, verbose_name='ARMEIRO', null=True)
    dataconcerto = models.DateField(blank=True, null=True, verbose_name='DATA DE CONCERTO')

    def __str__(self):
        return self.numeroseria

    def get_absolute_url(self):
        return reverse('home')


