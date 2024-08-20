from django.forms import ModelForm
from django import forms
from .models import Arma


class ArmaForm(ModelForm):
    class Meta:
        model = Arma
        fields = [
            'numeroserie',
            'cnpj',
            'numeropatri',
            'numerosinarm',
            'especie',
            'marca',
            'modelo',
            'calibre',
            'capacidade',
            'qtcarregador',
            'funcionamento',
            'acabamento',
            'qtcanos',
            'compricanos',
            'tipoalma',
            'qtraias',
            'sentidorais',
            'paisfabricacao',
            'acessorios',
            'docregistro',
            'tipomunicao',
            'datacompra',
            'unidade',
            'servidor',
            'gensmunicao',
            'qtmunicao',
            'observacoes',
            'matricula',
            'telefone',
            'datacautela',
            'numerosgpe',
            'docregistro',
            'responsavel',
        ]


class ArmaFormUpdate(ModelForm):
    class Meta:
        model = Arma
        fields = [
            'numeroserie',
            'cnpj',
            'numeropatri',
            'numerosinarm',
            'especie',
            'marca',
            'modelo',
            'calibre',
            'capacidade',
            'qtcarregador',
            'funcionamento',
            'acabamento',
            'qtcanos',
            'compricanos',
            'tipoalma',
            'qtraias',
            'sentidorais',
            'paisfabricacao',
            'acessorios',
            'docregistro',
            'tipomunicao',
            'datacompra',
            'unidade',
            'servidor',
        ]


class ArmaFormCautela(ModelForm):
    class Meta:
        model = Arma
        fields = [
            'numeroserie',
            'numeropatri',
            'numerosinarm',
            'marca',
            'modelo',
            'calibre',
            'capacidade',
            'qtcarregador',
            'acessorios',
            'tipomunicao',
            'gensmunicao',
            'unidade',
            'servidor',
            'matricula',
            'telefone',
            'datacautela',
            'numerosgpe',
            'responsavel',
            'observacoes',
            'qtmunicao',
            'tipo',
        ]


class ArmaForm(forms.ModelForm):
    class Meta:
        model = Arma
        fields = [
            'numeroserie',
            'numeropatri',
            'numerosinarm',
            'marca',
            'modelo',
            'calibre',
            'capacidade',
            'qtcarregador',
            'acessorios',
            'tipomunicao',
            'gensmunicao',
            'unidade',
            'servidor',
            'matricula',
            'telefone',
            'datacautela',
            'numerosgpe',
            'responsavel',
            'observacoes',
            'qtmunicao',
        ]      
