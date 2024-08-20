from django.db import models
from django.contrib.auth.models import User
from unidade.models import Unidade


class Servidor(models.Model):
    nome = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT)
    email = models.CharField(max_length=90)
    telefone = models.CharField(max_length=30)
    matricula = models.CharField(max_length=12)

    def __str__(self):
        return self.matricula
