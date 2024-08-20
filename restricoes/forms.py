from django.forms import ModelForm
from .models import Restricoes


class RestricoesForm(ModelForm):
    class Meta:
        model = Restricoes
        fields = [
            'serie', 'patrimonio', 'especie', 'marca', 'modelo',
            'servidor', 'matricula', 'lotacao', 'sgperecebimento', 
            'situacao', 'tipo', 'atualizacao', 'motivo',
            'responsavelcadastramento', 'datacadastramento', 'obsevacoes',
        ]


class RestricoesFormUpdate(ModelForm):
    class Meta:
        model = Restricoes
        fields = [
            'serie', 'patrimonio', 'sinarm', 'especie', 'marca', 'modelo',
            'calibre', 'servidor', 'telefone', 'cargo', 'matricula',
            'lotacao', 'sgperecebimento', 'situacao', 'tipo', 'datacautela',
            'atualizacao', 'historico', 'local', 'motivo', 'prazo',
            'responsavelcadastramento', 'datacadastramento', 'responsavelrecebimento',
            'datarecebimento', 'responsaveldevolucao', 'datadevolucao', 'obsevacoes',
        ]


class RestricoesFormCautela(ModelForm):
    class Meta:
        model = Restricoes
        fields = [
            'serie', 'patrimonio', 'especie', 'marca', 'modelo', 'calibre', 'servidor', 'telefone', 'cargo',
            'matricula', 'lotacao', 'situacao', 'responsavelrecebimento', 'datarecebimento', 'responsaveldevolucao',
            'datadevolucao', 'obsevacoes',
        ]