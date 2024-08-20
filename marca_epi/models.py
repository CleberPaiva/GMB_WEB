from django.db import models
from django.urls import reverse


class MarcaEpi(models.Model):
    marcaEpi = models.CharField(max_length=30, verbose_name='MARCA EPI')

    def __str__(self):
        return self.marcaEpi

    def get_absolute_url(self):
        return reverse('marca_epi_tabela')