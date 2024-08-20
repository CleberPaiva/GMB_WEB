from django.contrib import admin
from .models import Arma


class ListandoArmas(admin.ModelAdmin):
    search_fields = ('numeroserie', 'numeropatri', 'numerosinarm', 'modelo', 'calibre', 'servidor', 'unidade',
                     'datacautela', 'situacao', 'regional')
    list_display = ('numeroserie', 'numeropatri', 'modelo', 'calibre', 'servidor', 'unidade',
                    'datacautela', 'situacao', 'regional')
    list_filter = ('situacao', 'datacautela', 'regional', 'modelo', 'tipo', 'calibre', 'unidade')


admin.site.register(Arma, ListandoArmas)
