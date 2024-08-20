from django.views.generic.edit import CreateView
from .models import Mensagem
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


class MensagemCreate(CreateView):
    model = Mensagem
    fields = [
        'nome',
        'email',
        'mural',
    ]


@login_required
def mensagem_list(request):
    mensagem_list = Mensagem.objects.order_by("nome")
    busca = request.GET.get('busca')
    if busca:
        mensagem_list = Mensagem.objects.order_by("nome").filter(nome__icontains=busca) | \
            Mensagem.objects.order_by("nome").filter(mensagem__icontains=busca)

    paginator = Paginator(mensagem_list, 5)

    page = request.GET.get('page')
    mensagens = paginator.get_page(page)
    return render(request, 'mural/mural_list.html', {'mensagens': mensagens})
