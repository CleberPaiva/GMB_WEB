from django.db import models
from django.urls import reverse


class MarcaArma(models.Model):
    marcaArma = models.CharField(max_length=30, verbose_name='MARCA ARMA')

    def __str__(self):
        return self.marcaArma

    def get_absolute_url(self):
        return reverse('marca_arma_tabela')
