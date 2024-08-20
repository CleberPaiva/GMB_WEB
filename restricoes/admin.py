from django.contrib import admin
from .models import Restricoes


class ListandoRestricoes(admin.ModelAdmin):
    search_fields = ('serie', 'patrimonio', 'especie', 'modelo', 'calibre', 'servidor', 'cargo', 'matricula',
                     'datacadastramento', 'datarecebimento', 'datadevolucao',)
    list_display = ('serie', 'patrimonio', 'especie', 'modelo', 'calibre', 'servidor', 'cargo', 'matricula',
                    'datacadastramento', 'datarecebimento', 'datadevolucao',)
    list_filter = ('motivo', 'especie', 'marca', 'modelo', 'situacao', 'tipo', 'datacadastramento',
                   'datarecebimento', 'datadevolucao',)


admin.site.register(Restricoes, ListandoRestricoes)