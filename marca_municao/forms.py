from django.forms import ModelForm
from .models import MarcaMunicao


class MarcaMunicaoForm(ModelForm):
    class Meta:
        model = MarcaMunicao
        fields = [
            'marcaMunicao',
        ]


class MarcaMunicaoFormUpdate(ModelForm):
    class Meta:
        model = MarcaMunicao
        fields = [
            'marcaMunicao',
        ]

