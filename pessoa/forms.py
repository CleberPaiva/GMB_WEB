from django.forms import ModelForm
from .models import Pessoa


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = [
            'nome',
            'user',
            'unidade',
            'matricula',
            'cpf',
            'endereco',
            'telefone',
            'email',
            'funcao'
        ]


class PessoaFormUpdate(ModelForm):
    class Meta:
        model = Pessoa
        fields = [
            'nome',
            'user',
            'unidade',
            'matricula',
            'cpf',
            'endereco',
            'telefone',
            'email',
            'funcao'
        ]
