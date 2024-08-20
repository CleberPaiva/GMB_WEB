from django.forms import ModelForm
from .models import Mural


class MensagemForm(ModelForm):
    class Meta:
        model = Mural
        fields = [
            'destinatario',
            'mensagem',
            'remetente',
        ]
