from django.db import models
from django.urls import reverse
from unidade.models import Unidade


class Restricoes(models.Model):
    serie = models.CharField(max_length=40, verbose_name='Nº SÉRIE')
    patrimonio = models.CharField(max_length=40, verbose_name='Nº PATRIMÔNIO')
    sinarm = models.CharField(blank=True, null=True, max_length=40, verbose_name='Nº SINARM')
    especie = models.CharField(max_length=40, verbose_name='ESPÉCIE')
    marca = models.CharField(max_length=40, verbose_name='MARCA')
    modelo = models.CharField(max_length=40, verbose_name='MODELO')
    calibre = models.CharField(max_length=40, blank=True, null=True, verbose_name='CALIBRE')
    servidor = models.CharField(max_length=40, verbose_name='SERVIDOR')
    telefone = models.CharField(max_length=40, blank=True, null=True, verbose_name='TELEFONE')
    cargo = models.CharField(max_length=40, blank=True, null=True, verbose_name='CARGO')
    matricula = models.CharField(max_length=40, verbose_name='MATRÍCULA')
    lotacao = models.ForeignKey(Unidade, on_delete=models.PROTECT, related_name='LOTAÇÃO', db_column='lotacao')
    sgperecebimento = models.CharField(max_length=40, verbose_name='SGPE COMUNICAÇÃO')
    situacao = models.CharField(max_length=40, blank=True, null=True, verbose_name='SITUAÇÃO')
    tipo = models.CharField(max_length=40, blank=True, null=True, verbose_name='TIPO')
    datacautela = models.DateField(blank=True, null=True, verbose_name='DATA DA CAUTELA')
    atualizacao = models.CharField(max_length=40, blank=True, null=True, verbose_name='ATUALIZAÇÃO')
    historico = models.TextField(blank=True, null=True, verbose_name='HISTÓRICO')
    local = models.CharField(max_length=40, blank=True, null=True, verbose_name='SITUAÇÃO')
    motivo = models.CharField(max_length=40, verbose_name='MOTIVO')
    prazo = models.CharField(max_length=40, blank=True, null=True, verbose_name='PRAZO')
    responsavelcadastramento = models.CharField(max_length=40, verbose_name='RESPONSÁVEL CADASTRO')
    datacadastramento = models.DateField(blank=True, null=True, verbose_name='DATA CADASTRO')
    responsavelrecebimento = models.CharField(max_length=40, blank=True, null=True, verbose_name='REPONSÁVEL RECEBIMENTO')
    datarecebimento = models.DateField(blank=True, null=True, verbose_name='DATA RECEBIMENTO')
    responsavelentrega = models.CharField(max_length=120, blank=True, null=True, verbose_name='RESPONSÁVEL ENTREGA')
    responsaveldevolucao = models.CharField(max_length=40, blank=True, null=True, verbose_name='RESPONSÁVEL DEVOLUÇÃO')
    datadevolucao = models.DateField(blank=True, null=True, verbose_name='DATA DEVOLUÇÃO')
    obsevacoes = models.CharField(max_length=40,  blank=True, null=True, verbose_name='OBSERVAÇÕES')
    sgpedevolucao = models.CharField(max_length=40, blank=True, null=True, verbose_name='SGPE DEVOLUÇÃO')

    def __str__(self):
        return self.serie

    def get_absolute_url(self):
        return reverse('restricoes_list')