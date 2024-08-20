from django.views.generic.edit import CreateView
from .models import Mural
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse_lazy


class MuralCreate(CreateView):
    model = Mural
    fields = [
        'destinatario',
        'mensagem',
        'remetente',
    ]

    def get_success_url(self):
        return reverse_lazy('mural_list')    


@login_required
def mural_list(request):
    mural_list = Mural.objects.order_by("-created_at")
    busca = request.GET.get('busca')
    if busca:
        mural_list = Mural.objects.order_by("destinatario").filter(destinatario__icontains=busca) | \
            Mural.objects.order_by("mensagem").filter(mensagem__icontains=busca)

    paginator = Paginator(mural_list, 5)

    page = request.GET.get('page')
    murals = paginator.get_page(page)
    return render(request, 'mural/mural_list.html', {'murals': murals})
