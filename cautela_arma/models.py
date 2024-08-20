from django.db import models
from django.urls import reverse
from arma.models import Arma
from servidor.models import Servidor
from unidade.models import Unidade


class Cautela(models.Model):
    datacautela = models.DateField(blank=True, null=True, verbose_name='DATA DA CAUTELA')
    numerosgpe = models.CharField(max_length=30, blank=True, null=True, verbose_name='NUMERO SGPE')
    responsavel = models.CharField(max_length=140, blank=True, null=True, verbose_name='RESPONSAVEL')
    numeroserie = models.ForeignKey(Arma, on_delete=models.PROTECT)
    datadevolucao = models.DateField(blank=True, null=True, verbose_name='DATA DA DEVOLUÇÃO')
    servidor = models.ForeignKey(Servidor, on_delete=models.PROTECT)
    unidade = models.CharField(max_length=140, blank=True, null=True, verbose_name='UNIDADE')
    matricula = models.CharField(max_length=12, blank=True, null=True, verbose_name='MATRÍCULA')
    telefone = models.CharField(max_length=18, blank=True, null=True, verbose_name='TELEFONE')
    numeropatri = models.CharField(max_length=15, blank=True, null=True, verbose_name='Nº PATRIMÔNIO')
    numerosinarm = models.CharField(max_length=30, blank=True, null=True, verbose_name='Nº SINARM')
    especie = models.CharField(max_length=50, blank=True, null=True, verbose_name='ESPÉCIE')
    modelo = models.CharField(max_length=30, blank=True, null=True, verbose_name='MODELO')
    calibre = models.CharField(max_length=30, blank=True, null=True, verbose_name='CALIBRE')
    observacao = models.CharField(max_length=250, blank=True, null=True, verbose_name='OBSERVAÇÃO')
    marca = models.CharField(max_length=80, blank=True, null=True, verbose_name='MARCA')
    capacidade = models.CharField(max_length=10, blank=True, null=True, verbose_name='CAPACIDADE')
    qtcarregador = models.CharField(max_length=25, blank=True, null=True, verbose_name='CARREGADORES')
    docregistro = models.CharField(max_length=250, blank=True, null=True, verbose_name='DOC DE REGISTRO')
    tipo = models.CharField(max_length=30, blank=True, null=True, verbose_name='TIPO')
    regional = models.CharField(max_length=150, blank=True, null=True, verbose_name='REGIONAL')
    status = models.CharField(max_length=15, blank=True, null=True, verbose_name='STATUS')
    acessorios = models.CharField(max_length=250, blank=True, null=True, verbose_name='ACESSÓRIOS')    

    def __str__(self):
        return self.numerosgpe
