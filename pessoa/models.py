from django.db import models
from django.contrib.auth.models import User
from unidade.models import Unidade


class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    user = models.CharField(max_length=15, blank=True, null=True, verbose_name='USER')
    unidade = models.CharField(max_length=200, blank=True, null=True, verbose_name='UNIDADE')
    matricula = models.CharField(max_length=15, blank=True, null=True, verbose_name='MATRICULA')
    cpf = models.CharField(max_length=15, blank=True, null=True, verbose_name='CPF')
    endereco = models.CharField(max_length=200, blank=True, null=True, verbose_name='ENDEREÇO')
    telefone = models.CharField(max_length=50, blank=True, null=True, verbose_name='TELEFONE')
    email = models.CharField(max_length=120, blank=True, null=True, verbose_name='EMAIL')
    funcao = models.CharField(max_length=100, blank=True, null=True, verbose_name='FUNÇÃO')
    cidade = models.CharField(max_length=200, blank=True, null=True, verbose_name='CIDADE')

    def __str__(self):
        return self.nome
