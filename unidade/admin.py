from django.contrib import admin
from .models import Unidade


class ListandoUnidade(admin.ModelAdmin):
    search_fields = ('nome', 'telefone', 'email', 'endereco', 'gestor', 'orgao')
    list_display = ('nome', 'telefone', 'email', 'endereco', 'gestor', 'orgao')
    list_filter = ['orgao']


admin.site.register(Unidade, ListandoUnidade)

