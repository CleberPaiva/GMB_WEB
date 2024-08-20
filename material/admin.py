from django.contrib import admin
from .models import Material

class MaterialAdmin(admin.ModelAdmin):
    list_filter = ['especie']  # Adiciona filtros para iis, serie, especie
    search_fields = ('iis', 'serie', 'especie')  # Adiciona a pesquisa para iis, serie, especie

admin.site.register(Material, MaterialAdmin)
