from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from mural.models import Mural
from django.core.paginator import Paginator
from arma.models import Arma
from colete.models import Colete
from material.models import Material
from oficina.models import Oficina

import datetime


@login_required
def home(request):
    start_date = datetime.datetime(2023, 1, 1)
    armas_recentes = Arma.objects.filter(
        datacautela__gte=start_date
    ).count()
    armas_recentes_apx = Arma.objects.filter(
        datacautela__gte=start_date)\
        .filter(modelo='APX').count()
    armas_recentes_th9 = Arma.objects.filter(
        datacautela__gte=start_date)\
        .filter(modelo='TH9').count()
    arma_ano = Arma.objects.filter(
        datacautela__gt=datetime.datetime.now()-datetime.timedelta(days=365)
    ).count()
    coletes_recentes = Colete.objects.filter(
        datacautela__gte=start_date
    ).count()
    colete_ano = Colete.objects.filter(
        datacautela__gt=datetime.datetime.now()-datetime.timedelta(days=365)
    ).count()
    materiais_recentes = Material.objects.filter(
        datacautela__gt=datetime.datetime.now()-datetime.timedelta(days=30)
    ).count()
    materiais_ano = Material.objects.filter(
        datacautela__gt=datetime.datetime.now()-datetime.timedelta(days=365)
    ).count()
    oficina_ano = Oficina.objects.filter(
        dataentrada__gt=datetime.datetime.now()-datetime.timedelta(days=365)
    ).count()
    return render(request, 'core/index.html', {'armas_recentes': armas_recentes,
                                               'arma_ano': arma_ano,
                                               'coletes_recentes': coletes_recentes,
                                               'materiais_recentes': materiais_recentes,
                                               'materiais_ano': materiais_ano,
                                               'oficina_ano': oficina_ano,
                                               'colete_ano': colete_ano,
                                               'armas_recentes_apx': armas_recentes_apx,
                                               'armas_recentes_th9': armas_recentes_th9})


@login_required
def fabricantes(request):
    data = {'usuario': request.user}
    return render(request, 'core/fabricantes.html', data)


@login_required
def cadastros(request):
    data = {'usuario': request.user}
    return render(request, 'core/cadastros.html', data)


@login_required
def estoque(request):
    data = {'usuario': request.user}
    return render(request, 'core/estoque.html', data)


@login_required
def municoes(request):
    data = {'usuario': request.user}
    return render(request, 'core/municoes.html', data)


@login_required
def mural_tabela(request):
    mural_tabela = Mural.objects.order_by("destinatario")
    paginator = Paginator(mural_tabela, 10)

    page = request.GET.get('page')
    murals = paginator.get_page(page)
    return render(request, 'mural/mural_list.html', {'murals': murals})
