from django.forms import ModelForm
from .models import MarcaEpi


class MarcaEpiForm(ModelForm):
    class Meta:
        model = MarcaEpi
        fields = [
            'marcaEpi',
        ]


class MarcaEpiFormUpdate(ModelForm):
    class Meta:
        model = MarcaEpi
        fields = [
            'marcaEpi',
        ]

