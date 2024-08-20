from django.db import models
from material.models import Material
from unidade.models import Unidade 


class CautelaMaterialTotal(models.Model):
    data_cautela = models.DateField(blank=True, null=True, verbose_name='DATA') 
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, related_name='cautela_materiais')
    responsavel = models.CharField(max_length=255) 
    matricula = models.CharField(max_length=50)
    sgpe = models.CharField(max_length=50) 

    def __str__(self):
        return self.sgpe 


class MaterialCautelaTotal(models.Model):
    material_geral = models.ForeignKey(Material, on_delete=models.PROTECT)
    cautela_material = models.ForeignKey(CautelaMaterialTotal, on_delete=models.PROTECT)
    serie = models.CharField(max_length=15, blank=True, null=True)
    especie = models.CharField(max_length=30, blank=True, null=True)
    modelo = models.CharField(max_length=30, blank=True, null=True)
    fabricante = models.CharField(max_length=30, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')

    def __str__(self):
        return str(self.material_geral)