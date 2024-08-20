from django.contrib import admin
from .models import Pessoa


class ListandoPessoas(admin.ModelAdmin):
    search_fields = ('nome', 'unidade', 'matricula', 'cpf', 'funcao', 'cidade')
    list_display = ('nome', 'unidade', 'matricula', 'cpf', 'funcao', 'cidade')
    list_filter = ('funcao', 'unidade', 'cidade')


admin.site.register(Pessoa, ListandoPessoas)



