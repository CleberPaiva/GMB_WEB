from django.contrib import admin
from .models import Municao


class ListandoMunicao(admin.ModelAdmin):
    search_fields = ('gens', 'calibre', 'tipo', 'quantidade', 'nome', 'matricula', 'data', 'sgpe', 'responsavel', 'unidade', 'observacoes')
    list_display = ('gens', 'calibre', 'tipo', 'quantidade', 'nome', 'matricula', 'data', 'sgpe', 'responsavel', 'unidade', 'observacoes')
    list_filter = ('gens', 'calibre', 'tipo', 'quantidade', 'nome', 'matricula', 'data', 'sgpe', 'responsavel', 'unidade', 'observacoes')


admin.site.register(Municao, ListandoMunicao)
