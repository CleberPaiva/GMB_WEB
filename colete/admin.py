from django.contrib import admin
from .models import Colete


class ListandoColetes(admin.ModelAdmin):
    search_fields = ('numeroserie', 'numeropatri', 'pais', 'servidor', 'cargo', 'unidade', 'datacautela', 'modelo')
    list_display = ('numeroserie', 'numeropatri', 'servidor', 'datacautela', 'unidade', 'tipo', 'especie')
    list_filter = ('datacautela', 'unidade', 'tipo', 'especie')


admin.site.register(Colete, ListandoColetes)
