from django.forms import ModelForm
from .models import Fornecedor


class FornecedorForm(ModelForm):
    class Meta:
        model = Fornecedor
        fields = [
            'nomefantasia',
            'razaosocial',
            'endereco',
            'telefone',
            'email',
        ]


class FornecedorFormUpdate(ModelForm):
    class Meta:
        model = Fornecedor
        fields = [
            'nomefantasia',
            'razaosocial',
            'endereco',
            'telefone',
            'email',
        ]
