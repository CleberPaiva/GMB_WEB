from django.forms import ModelForm
from .models import Cautela


class CautelaForm(ModelForm):
    class Meta:
        model = Cautela
        fields = [
            'datacautela',
            'numerosgpe',
            'responsavel',
            'numeroserie',
            'datadevolucao',
            'servidor',
            'unidade',
        ]


class CautelaFormUpdate(ModelForm):
    class Meta:
        model = Cautela
        fields = [
            'datacautela',
            'numerosgpe',
            'responsavel',
            'numeroserie',
            'datadevolucao',
            'servidor',
            'unidade',
        ]


class CautelaFormCautela(ModelForm):
    class Meta:
        model = Cautela
        fields = [
            'datacautela',
            'numerosgpe',
            'responsavel',
            'numeroserie',
            'datadevolucao',
            'servidor',
            'unidade',
        ]
