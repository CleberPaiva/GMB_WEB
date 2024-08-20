from django.db import models
from django.urls import reverse
from unidade.models import Unidade
from django.contrib.auth.models import User


class Municao(models.Model):
    gens = models.CharField(max_length=30, verbose_name='GENS')
    calibre = models.CharField(max_length=30, blank=True, null=True, verbose_name='CALIBRE')
    tipo = models.CharField(max_length=30, blank=True, null=True, verbose_name='TIPO')
    marca = models.CharField(max_length=30, blank=True, null=True, verbose_name='MARCA')
    quantidade = models.CharField(max_length=30, verbose_name='QUANTIDADE')
    nome = models.CharField(max_length=30, verbose_name='NOME')
    matricula = models.CharField(max_length=20, blank=True, null=True, verbose_name='MATRICULA')
    data = models.DateField(blank=True, null=True, verbose_name='DATA')
    sgpe = models.CharField(max_length=30, verbose_name='SGPE')
    responsavel = models.CharField(max_length=30, verbose_name='RESPONSÁVEL')
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT)
    observacoes = models.CharField(max_length=1200, blank=True, null=True, verbose_name='OBSERVAÇÕES')

    def __str__(self):
        return self.gens

    def get_absolute_url(self):
        return reverse('municao_list')