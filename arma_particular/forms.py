from django.forms import ModelForm
from django import forms
from .models import ArmaParticular


class ArmaParticularForm(ModelForm):
    class Meta:
        model = ArmaParticular
        fields = [
            'numeroserie',
            'nome',
            'cpf',
            'rg',
            'numerosigma',
            'numerosinarm',
            'numeroregistro',
            'amparo',
            'tipo',
            'marca',
            'calibre',
            'dataexpedicao',
            'datavalidade',
            'imagem',
            'imagem2',
            'imagem3',
        ]


class ArmaParticularFormUpdate(ModelForm):
    class Meta:
        model = ArmaParticular
        fields = [
            'numeroserie',
            'cpf',
            'rg',
            'numerosigma',
            'numerosinarm',
            'numeroregistro',
            'amparo',
            'tipo',
            'marca',
            'calibre',
            'dataexpedicao',
            'datavalidade',
            'documento',
            'imagem',
            'imagem2',
            'imagem3',
        ]


class ArmaParticularFormCautela(ModelForm):
    class Meta:
        model = ArmaParticular
        fields = [
            'numeroserie',
            'cpf',
            'rg',
            'numerosigma',
            'numerosinarm',
            'numeroregistro',
            'amparo',
            'tipo',
            'marca',
            'calibre',
            'dataexpedicao',
            'datavalidade',
            'documento',
            'imagem',
            'imagem2',
            'imagem3',
        ]
