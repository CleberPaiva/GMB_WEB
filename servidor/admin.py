from django.contrib import admin
from cautela_arma.models import Cautela
from .models import Servidor


class CautelaInline(admin.TabularInline):
    model = Cautela


class ServidorAdmin(admin.ModelAdmin):
    inlines = (CautelaInline, )
    list_display = ('nome', 'user', 'telefone', 'email')
    search_fields = ['nome']
    list_filter = ['unidade']


class ListandoServidores(admin.ModelAdmin):
    search_fields = ('nome', 'unidade', 'user', 'email', 'telefone')
    list_display = ('nome', 'user', 'telefone', 'email')
    list_filter = ['unidade']


admin.site.register(Servidor, ServidorAdmin)

