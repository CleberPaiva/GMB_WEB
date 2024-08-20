from django.db import models
from django.urls import reverse


class Mural(models.Model):
    destinatario = models.CharField(max_length=50, verbose_name='Destinatario')
    mensagem = models.CharField(max_length=3000, verbose_name='Mensagem')
    remetente = models.CharField(max_length=50, verbose_name='Remetente')
    created_at = models.DateTimeField(auto_now_add=True)
    imagem_mural = models.ImageField(upload_to='mural/', blank=True, null=True)
    imagem2_mural = models.ImageField(upload_to='mural/', blank=True, null=True)
    resposta = models.CharField(max_length=3000, blank=True, null=True, verbose_name='Resposta')

    def __str__(self):
        return self.destinatario

    def get_absolute_url(self):
        return reverse('create_mural')
