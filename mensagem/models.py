from django.db import models
from django.urls import reverse


class Mensagem(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    email = models.CharField(max_length=80, verbose_name='Email')
    mensagem = models.CharField(max_length=200, verbose_name='Mensagem')


    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('create_mensagem')
