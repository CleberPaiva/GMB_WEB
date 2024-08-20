from django.db import models
from django.urls import reverse


class Material(models.Model):
    iis = models.CharField(max_length=10, blank=True, null=True, verbose_name='NUMERO DE SÉRIE')
    serie = models.CharField(max_length=15, blank=True, null=True, verbose_name='CNPJ')
    especie = models.CharField(max_length=30, blank=True, null=True, verbose_name='Nº PATRIMÔNIO')
    modelo = models.CharField(max_length=30, blank=True, null=True, verbose_name='Nº SINARM')
    fabricante = models.CharField(max_length=30, blank=True, null=True, verbose_name='ESPÉCIE')
    material = models.CharField(max_length=30, blank=True, null=True, verbose_name='ESPÉCIE')
    cor = models.CharField(max_length=15, blank=True, null=True, verbose_name='MODELO')
    altura = models.CharField(max_length=10, blank=True, null=True, verbose_name='CALIBRE')
    largura = models.CharField(max_length=10, blank=True, null=True, verbose_name='CAPACIDADE')
    pesoliquido = models.CharField(max_length=10, blank=True, null=True, verbose_name='QUANTIDADE DE CARREGADORES')
    pesobruto = models.CharField(max_length=10, blank=True, null=True, verbose_name='FUNCIONAMENTO')
    retardo = models.CharField(max_length=15, blank=True, null=True, verbose_name='ACABAMENTO')
    duploestagio = models.CharField(max_length=15, blank=True, null=True, verbose_name='QUANTIDADE DE CANOS')
    unidade = models.CharField(max_length=150, blank=True, null=True, verbose_name='UNIDADE')
    situacao = models.CharField(max_length=30, blank=True, null=True, verbose_name='SITUAÇÃO')
    sgpecautela = models.CharField(max_length=30, blank=True, null=True, verbose_name='SGPE CAUTELA')
    datacautela = models.DateField(blank=True, null=True, verbose_name='DATA DA CAUTELA')
    sgpetroca = models.CharField(max_length=30, blank=True, null=True, verbose_name='SGPE TROCA')
    datatroca = models.DateField(blank=True, null=True, verbose_name='DATA DA TROCA')
    quantidade = models.IntegerField(blank=True, null=True, verbose_name='QUANTIDADE')
 
    def __str__(self):
        return self.iis


class Municao(models.Model):
    gens = models.CharField(max_length=30, verbose_name='GENS')
    calibre = models.CharField(max_length=30, verbose_name='CALIBRE')
    modelo = models.CharField(max_length=30, verbose_name='MODELO')
    fabricante = models.CharField(max_length=30, verbose_name='ESPÉCIE')
    qtdcaixas = models.IntegerField(verbose_name='QTD CAIXAS')
    qtdproduto = models.IntegerField(verbose_name="QTD PRODUTO")

    def __str__(self):
        return self.modelo

    def get_absolute_url(self):
        return reverse('municao_list')


class Projetil(models.Model):
    gens = models.CharField(max_length=30, verbose_name='GENS')
    calibre = models.CharField(max_length=30, verbose_name='CALIBRE')
    modelo = models.CharField(max_length=30, verbose_name='MODELO')
    fabricante = models.CharField(max_length=30, verbose_name='ESPÉCIE')
    qtdcaixas = models.IntegerField(verbose_name='QTD CAIXAS')
    qtdproduto = models.IntegerField(verbose_name="QTD PRODUTO")

    def __str__(self):
        return self.modelo

    def get_absolute_url(self):
        return reverse('projetil_tabela')
