from django.contrib import admin
from .models import Cautela


class ListandoCautelas(admin.ModelAdmin):
    search_fields = ('datacautela', 'servidor', 'numeroserie', 'matricula', 'responsavel')
    list_display = ('datacautela', 'servidor', 'matricula', 'numeroserie', 'datadevolucao')
    list_filter = ('responsavel', 'datacautela', 'datadevolucao')


admin.site.register(Cautela, ListandoCautelas)
