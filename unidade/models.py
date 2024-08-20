from django.db import models
from django.urls import reverse


class Unidade(models.Model):
    nome = models.CharField(max_length=80, verbose_name='NOME')
    telefone = models.CharField(max_length=30, verbose_name='TELEFONE')
    email = models.CharField(max_length=50, verbose_name='E-MAIL')
    endereco = models.CharField(max_length=150, verbose_name='ENDEREÇO')
    gestor = models.CharField(max_length=40, verbose_name='GESTOR')
    orgao = models.CharField(max_length=40, verbose_name='ÓRGÃO')

    def __str__(self):
            return str(self.nome)

    def get_absolute_url(self):
        return reverse('home')
