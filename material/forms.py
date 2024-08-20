from django.forms import ModelForm
from .models import Material, Municao


class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = [
            'iis',
            'serie',
            'especie',
            'modelo',
            'fabricante',
            'material',
            'cor',
            'altura',
            'largura',
            'pesoliquido',
            'pesobruto',
            'retardo',
            'duploestagio',
            'unidade',
            'situacao',
            'sgpecautela',
            'datacautela',
            'sgpetroca',
            'datatroca',
        ]


class MaterialFormUpdate(ModelForm):
    class Meta:
        model = Material
        fields = [
            'iis',
            'serie',
            'especie',
            'modelo',
            'fabricante',
            'material',
            'cor',
            'altura',
            'largura',
            'pesoliquido',
            'pesobruto',
            'retardo',
            'duploestagio',
            'unidade',
            'situacao',
            'sgpecautela',
            'datacautela',
            'sgpetroca',
            'datatroca',
        ]

class MunicaoForm(ModelForm):
    class Meta:
        model = Municao
        fields = [
            'gens',
            'calibre',
            'modelo',
            'fabricante',
            'qtdcaixas',
            'qtdproduto',
        ]
