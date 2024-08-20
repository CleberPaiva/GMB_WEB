from django.forms import ModelForm
from .models import Oficina


class OficinaForm(ModelForm):
    class Meta:
        model = Oficina
        fields = [
            'dataentrada',
            'datasaida',
            'numeroseria',
            'especie',
            'modelo',
            'cargapara',
            'unidade',
            'historico',
            'servico',
            'usuario',
            'armeiro',
            'dataconcerto'

        ]


class OficinaFormUpdate(ModelForm):
    class Meta:
        model = Oficina
        fields = [
            'servico',
            'armeiro',
            'dataconcerto'
        ]
