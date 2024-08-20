from django.forms import ModelForm
from django import forms
from .models import Municao


class MunicaoForm(ModelForm):
    class Meta:
        model = Municao
        fields = [
            'gens',
            'calibre',
            'tipo',
            'marca',
            'quantidade',
            'nome',
            'matricula',
            'data',
            'sgpe',
            'responsavel',
            'unidade',
            'observacoes',
        ]


class MunicaoFormUpdate(ModelForm):
    class Meta:
        model = Municao
        fields = [
            'gens',
            'calibre',
            'tipo',
            'marca',
            'quantidade',
            'nome',
            'matricula',
            'data',
            'sgpe',
            'responsavel',
            'unidade',
            'observacoes',
        ]


class MunicaoFormCautela(ModelForm):
    class Meta:
        model = Municao
        fields = [
            'gens',
            'calibre',
            'tipo',
            'marca',
            'quantidade',
            'nome',
            'matricula',
            'data',
            'sgpe',
            'responsavel',
            'unidade',
            'observacoes',
        ]