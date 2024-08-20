from django.forms import ModelForm
from .models import MarcaArma


class MarcaArmaForm(ModelForm):
    class Meta:
        model = MarcaArma
        fields = [
            'marcaArma',
        ]


class MarcaArmaFormUpdate(ModelForm):
    class Meta:
        model = MarcaArma
        fields = [
            'marcaArma',
        ]

