from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Arma(models.Model):
    numeroserie = models.CharField(max_length=30, verbose_name='NUMERO DE SÉRIE')
    cnpj = models.CharField(max_length=20, blank=True, null=True, verbose_name='CNPJ')
    numeropatri = models.CharField(max_length=20, blank=True, null=True, verbose_name='Nº PATRIMÔNIO')
    numerosinarm = models.CharField(max_length=20, blank=True, null=True, verbose_name='Nº SINARM')
    especie = models.CharField(max_length=30, verbose_name='ESPÉCIE')
    marca = models.CharField(max_length=30, verbose_name='MARCA')
    modelo = models.CharField(max_length=30, verbose_name='MODELO')
    calibre = models.CharField(max_length=30, verbose_name='CALIBRE')
    capacidade = models.CharField(max_length=30, verbose_name='CAPACIDADE')
    qtcarregador = models.CharField(max_length=30, verbose_name='QUANTIDADE DE CARREGADORES')
    funcionamento = models.CharField(max_length=20, verbose_name='FUNCIONAMENTO')
    acabamento = models.CharField(max_length=15, verbose_name='ACABAMENTO')
    qtcanos = models.CharField(max_length=10, verbose_name='QUANTIDADE DE CANOS')
    compricanos = models.CharField(max_length=15, verbose_name='COMPRIMENTO DE CANOS')
    tipoalma = models.CharField(max_length=10, verbose_name='TIPO DE ALMA')
    qtraias = models.CharField(max_length=10, verbose_name='QUANTIDADE DE RAIAS')
    sentidorais = models.CharField(max_length=10, verbose_name='SENTIDO DAS RAIAS')
    paisfabricacao = models.CharField(max_length=30, verbose_name='PAIS DE FABRICAÇÃO')
    acessorios = models.CharField(max_length=100, verbose_name='ACESSORIOS')
    docregistro = models.CharField(max_length=150,blank=True, null=True, verbose_name='DOCUMENTO DE REGISTRO')
    tipomunicao = models.CharField(max_length=30, verbose_name='TIPO DE MUNIÇÃO')
    datacompra = models.DateField(blank=True, null=True, verbose_name='DATA DA COMPRA')
    unidade = models.CharField(max_length=150, blank=True, null=True, verbose_name='UNIDADE')
    servidor = models.CharField(max_length=150, blank=True, null=True, verbose_name='SERVIDOR')
    gensmunicao = models.CharField(max_length=50, blank=True, null=True, verbose_name='GENS DA MUNIÇÃO')
    qtmunicao = models.CharField(max_length=10, blank=True, null=True, verbose_name='QUANTIDADE DE MUNIÇÃO')
    observacoes = models.CharField(max_length=150, blank=True, null=True, verbose_name='OBSERVAÇÕES')
    matricula = models.CharField(max_length=150, blank=True, null=True, verbose_name='MATRICULA')
    telefone = models.CharField(max_length=80, blank=True, null=True, verbose_name='TELEFONE')
    datacautela = models.DateField(blank=True, null=True, verbose_name='DATA DA CAUTELA')
    numerosgpe = models.CharField(max_length=30, blank=True, null=True, verbose_name='NUMERO SGPE')
    responsavel = models.CharField(max_length=140, blank=True, null=True, verbose_name='RESPONSAVEL')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    tipo = models.CharField(max_length=30, blank=True, null=True, verbose_name='TIPO')
    situacao = models.CharField(max_length=40, blank=True, null=True, verbose_name='SITUAÇÂO')
    regional = models.CharField(max_length=80, blank=True, null=True, verbose_name='REGIONAL')
    datadevolucao = models.DateField(blank=True, null=True, verbose_name='DATA DA DEVOLUÇÃO')

    def __str__(self):
        return self.numeroserie

    def get_absolute_url(self):
        return reverse('arma_list')
