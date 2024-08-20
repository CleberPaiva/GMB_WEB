from django.db import models
from material.models import Material
from unidade.models import Unidade  # Assumindo que você tenha um modelo Unidade

class CautelaMaterial(models.Model):
    material_geral = models.ForeignKey(Material, on_delete=models.CASCADE)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)  # Relação ForeignKey com Unidade
    serie = models.CharField(max_length=15, blank=True, null=True)
    especie = models.CharField(max_length=30, blank=True, null=True)
    modelo = models.CharField(max_length=30, blank=True, null=True)
    fabricante = models.CharField(max_length=30, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)
    data_cautela = models.DateField(auto_now_add=True)  # Data da Cautela
    responsavel = models.CharField(max_length=255)  # Responsável
    matricula = models.CharField(max_length=50)  # Matrícula
    sgpe = models.CharField(max_length=50)  # Matrícula
    quantidade = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')


    def __str__(self):
        return self.material_geral.iis  # Retornando o campo `iis` do objeto `Material` associado.

