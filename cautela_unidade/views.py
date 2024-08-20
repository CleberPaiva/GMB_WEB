from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
#  from .models import Unidade
from unidade.models import Unidade
from arma.models import Arma
from colete.models import Colete


@login_required
def unidade_list(request):
    unidade_list = Unidade.objects.order_by("nome")
    busca = request.GET.get('busca')
    if busca:
        unidade_list = Unidade.objects.order_by("nome").filter(nome__icontains=busca)

    paginator = Paginator(unidade_list, 25)

    page = request.GET.get('page')
    unidades = paginator.get_page(page)
    return render(request, 'cautela_unidade/unidade_list.html', {'unidades': unidades})

@login_required
def unidade(request, pk):
    unidade = get_object_or_404(Unidade, pk=pk)
    armas = Arma.objects.filter(unidade=unidade).filter(servidor__in=["GESTOR", unidade])
    coletes = Colete.objects.filter(unidade=unidade).filter(servidor__in=["GESTOR", unidade]) 
    return render(request, 'cautela_unidade/unidade.html', {'unidade': unidade, 'armas': armas, 'coletes': coletes})
#    return render(request, 'cautela_unidade/unidade.html', {'unidade': unidade, 'armas': armas, 'coletes': coletes})

@login_required
def unidade_imprimir(request, pk):
    unidade = get_object_or_404(Unidade, pk=pk)
    armas = Arma.objects.filter(unidade=unidade).filter(servidor__in=["GESTOR", unidade])
    primeira_arma = armas[0]  # Pega o primeiro objeto Arma na lista
    regional = primeira_arma.regional  # Acessa o campo 'regional' do objeto Arma
    coletes = Colete.objects.filter(unidade=unidade).filter(servidor__in=["GESTOR", unidade]) 
    return render(request, 'cautela_unidade/unidade_imprimir.html', {'unidade': unidade, 'armas': armas, 'coletes': coletes, 'regional': regional})

