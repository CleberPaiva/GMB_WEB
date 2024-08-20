from django.contrib import admin
from .models import ArmaParticular


class ListandoArmaParticular(admin.ModelAdmin):
    search_fields = ('numeroserie', 'cpf', 'rg', 'numerosigma', 'numerosinarm', 'numeroregistro', 'amparo', 'tipo', 'calibre', 'datavalidade')
    list_display = ('numeroserie', 'cpf', 'rg', 'numerosigma', 'numerosinarm', 'numeroregistro', 'amparo', 'tipo', 'calibre', 'datavalidade')
    list_filter = ('numeroserie', 'cpf', 'rg', 'numerosigma', 'numerosinarm', 'numeroregistro', 'amparo', 'tipo', 'calibre', 'datavalidade')


admin.site.register(ArmaParticular, ListandoArmaParticular)
