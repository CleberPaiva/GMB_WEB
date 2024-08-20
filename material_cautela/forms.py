from django.forms import ModelForm
from django import forms
from .models import CautelaMaterialTotal
from .models import MaterialCautelaTotal


class MaterialTotalForm(ModelForm):
    class Meta:
        model = CautelaMaterialTotal
        fields = [
            'data_cautela',
            'unidade',
            'responsavel',
            'matricula',
            'sgpe',
        ]


class MaterialCautelaTotalForm(forms.ModelForm):
    class Meta:
        model = MaterialCautelaTotal
        fields = '__all__'

