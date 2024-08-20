from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class ArmaParticular(models.Model):
    numeroserie = models.CharField(max_length=30, verbose_name='NUMERO DE SÉRIE')
    nome = models.CharField(max_length=30, verbose_name='NOME')
    cpf = models.CharField(max_length=20, blank=True, null=True, verbose_name='Nº CPF')
    rg = models.CharField(max_length=20, blank=True, null=True, verbose_name='Nº RG')
    numerosigma = models.CharField(max_length=20, blank=True, null=True, verbose_name='Nº SIGMA')
    numerosinarm = models.CharField(max_length=20, blank=True, null=True, verbose_name='Nº SINARM')
    numeroregistro = models.CharField(max_length=20, blank=True, null=True, verbose_name='Nº REGISTRO')
    amparo = models.CharField(max_length=30, verbose_name='AMPARO LEGAL')
    tipo = models.CharField(max_length=30, verbose_name='TIPO')
    marca = models.CharField(max_length=30, verbose_name='MARCA')
    calibre = models.CharField(max_length=30, verbose_name='CALIBRE')
    dataexpedicao = models.DateField(blank=True, null=True, verbose_name='DATA DE EXPEDIÇÃO')
    datavalidade = models.DateField(blank=True, null=True, verbose_name='DATA DE VALIDADE')
    documento = models.FileField(upload_to='pdfs_arma_particular/', blank=True, null=True, verbose_name='PDF')
    imagem = models.ImageField(upload_to='pdfs_arma_particular/', blank=True, null=True)
    imagem2 = models.ImageField(upload_to='pdfs_arma_particular/', blank=True, null=True)
    imagem3 = models.ImageField(upload_to='pdfs_arma_particular/', blank=True, null=True)

    def __str__(self):
        return self.numeroserie

    def get_absolute_url(self):
        return reverse('arma_particular_list')
