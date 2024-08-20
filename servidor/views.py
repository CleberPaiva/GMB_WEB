from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Servidor
from arma.models import Arma
from colete.models import Colete


@login_required
def servidor_list(request):
    servidor_list = Servidor.objects.order_by("nome")
    busca = request.GET.get('busca')
    if busca:
        servidor_list = Servidor.objects.order_by("nome").filter(nome__icontains=busca)

    paginator = Paginator(servidor_list, 25)

    page = request.GET.get('page')
    servidors = paginator.get_page(page)
    return render(request, 'servidor/servidor_list.html', {'servidors': servidors})


@login_required
def servidor(request, pk):
    servidor = get_object_or_404(Servidor, pk=pk)
    armas = Arma.objects.filter(matricula=servidor)
    coletes = Colete.objects.filter(matricula=servidor)
    return render(request, 'servidor/servidor.html', {'servidor': servidor, 'armas': armas, 'coletes': coletes})


@login_required
def servidor_imprimir(request, pk):
    servidor = get_object_or_404(Servidor, pk=pk)
    armas = Arma.objects.filter(matricula=servidor)
    coletes = Colete.objects.filter(matricula=servidor)
    return render(request, 'servidor/servidor_imprimir.html', {'servidor': servidor, 'armas': armas, 'coletes': coletes})



