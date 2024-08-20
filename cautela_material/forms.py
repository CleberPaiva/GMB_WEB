from django import forms
from .models import CautelaMaterial

class CautelaMaterialForm(forms.ModelForm):
    class Meta:
        model = CautelaMaterial
        fields = ['unidade', 'responsavel', 'matricula', 'material_geral', 'serie', 
                  'especie', 'modelo', 'fabricante', 'quantidade', 'observacao', 'sgpe']
