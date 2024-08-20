from django.db import models
from django.urls import reverse


class MarcaMunicao(models.Model):
    marcaMunicao = models.CharField(max_length=30, verbose_name='MARCA MUNIÇÃO')

    def __str__(self):
        return self.marcaMunicao

    def get_absolute_url(self):
        return reverse('marca_municao_tabela')


