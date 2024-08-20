from django.db import models
from django.urls import reverse


class Colete(models.Model):
    numeroserie = models.CharField(max_length=40, verbose_name='NUMERO DE SÉRIE')
    cnpj = models.CharField(max_length=30, verbose_name='CNPJ')
    numeropatri = models.CharField(max_length=30, verbose_name='Nº PATRIMÔNIO')
    especie = models.CharField(max_length=50, verbose_name='ESPÉCIE')
    pais = models.CharField(max_length=30, verbose_name='PAÍS')
    marca = models.CharField(max_length=50, verbose_name='MARCA')
    nivel = models.CharField(max_length=50, verbose_name='NÍVEL')
    sexo = models.CharField(max_length=50, verbose_name='SEXO')
    tamanho = models.CharField(max_length=50, verbose_name='TAMANHO')
    modelo = models.CharField(max_length=50, blank=True, null=True, verbose_name='MODELO')
    lote = models.CharField(max_length=25, blank=True, null=True, verbose_name='LOTE')
    datafabricacao = models.DateField(blank=True, null=True, verbose_name='DATA DA FABRICAÇÃO')
    garantia = models.CharField(max_length=20, blank=True, null=True, verbose_name='GARANTIA')
    capa = models.CharField(max_length=200, blank=True, null=True, verbose_name='CAPA')
    servidor = models.CharField(max_length=150, blank=True, null=True, verbose_name='SERVIDOR')
    cargo = models.CharField(max_length=50, blank=True, null=True, verbose_name='CARGO')
    unidade = models.CharField(max_length=150, blank=True, null=True, verbose_name='UNIDADE')
    sgpe = models.CharField(max_length=50, blank=True, null=True, verbose_name='SGPE')
    situacao = models.CharField(max_length=100, blank=True, null=True, verbose_name='SITUAÇÃO')
    datacautela = models.DateField(blank=True, null=True, verbose_name='DATA DA CAUTELA')
    atualizacao = models.CharField(max_length=50, blank=True, null=True, verbose_name='ATUALIZAÇÃO')
    historico = models.CharField(max_length=600, blank=True, null=True, verbose_name='HISTÓRICO')
    matricula = models.CharField(max_length=300, blank=True, null=True, verbose_name='MATRICULA')
    tipo = models.CharField(max_length=300, blank=True, null=True, verbose_name='TIPO')
    datadevolucao = models.DateField(blank=True, null=True, verbose_name='DATA DA DEVOLUÇÃO')
    observacoes = models.CharField(max_length=1000, blank=True, null=True, verbose_name='OBSERVAÇÕES')

    def __str__(self):
        return self.numeroserie

    def get_absolute_url(self):
        return reverse('arma_list')