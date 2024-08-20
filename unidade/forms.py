from django.forms import ModelForm
from unidade.models import Unidade


class UnidadeForm(ModelForm):
    class Meta:
        model = Unidade
        fields = [
            'nome',
            'telefone',
            'email',
            'endereco',
            'gestor',
            'orgao',
        ]


class UnidadeFormUpdate(ModelForm):
    class Meta:
        model = Unidade
        fields = [
            'nome',
            'telefone',
            'email',
            'endereco',
            'gestor',
            'orgao',
        ]