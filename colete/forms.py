from django.forms import ModelForm
from .models import Colete
from unidade.models import Unidade


class ColeteForm(ModelForm):
    class Meta:
        model = Colete
        fields = [
            'numeroserie', 'cnpj', 'numeropatri', 'especie', 'pais', 'marca', 'nivel', 'sexo',
            'tamanho', 'modelo', 'lote', 'datafabricacao', 'garantia', 'capa', 'servidor', 'cargo',
            'unidade', 'sgpe', 'situacao', 'datacautela', 'atualizacao', 'historico', 'matricula', 'tipo', 'observacoes',
        ]


class ColeteFormUpdate(ModelForm):
    class Meta:
        model = Colete
        fields = [
            'numeroserie', 'cnpj', 'numeropatri', 'especie', 'pais', 'marca', 'nivel', 'sexo',
            'tamanho', 'modelo', 'lote', 'datafabricacao', 'garantia', 'capa', 'servidor', 'cargo',
            'unidade', 'sgpe', 'situacao', 'datacautela', 'atualizacao', 'historico', 'matricula', 'tipo', 'observacoes',
        ]


class ColeteFormCautela(ModelForm):
    class Meta:
        model = Colete
        fields = [
            'numeroserie', 'numeropatri', 'marca', 'especie', 'nivel', 'modelo', 'unidade', 'servidor',
            'matricula', 'cargo', 'garantia', 'capa', 'sgpe', 'datacautela', 'tipo', 'observacoes',
        ]