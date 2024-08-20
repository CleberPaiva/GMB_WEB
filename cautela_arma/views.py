from django.views.generic.edit import CreateView
from .models import Cautela
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import CautelaFormUpdate
from .forms import CautelaFormCautela
from django.core.paginator import Paginator
from unidade.models import Unidade
from servidor.models import Servidor
from arma.models import Arma
from django.http import JsonResponse
from django.core import serializers
import json


@method_decorator(login_required, name='dispatch')
class CautelaCreate(CreateView):
    model = Cautela
    fields = [
        'datacautela',
        'numerosgpe',
        'responsavel',
        'numeroserie',
        'datadevolucao',
        'servidor',
        'unidade',
        ]


@login_required
def cautela_edit(request, pk):
    cautela = get_object_or_404(Cautela, pk=pk)
    form = CautelaFormUpdate(instance=cautela)
    if request.method == 'POST':
        form = CautelaFormUpdate(request.POST, instance=cautela)

        if form.is_valid():
            cautela = form.save(commit=False)
            cautela.save()
            return redirect('/cautela_arma/list')
        else:
            return render(request, 'cautela_arma/cautela_edit.html', {'form': form, 'cautela': cautela})
    elif request.method == 'GET':
        return render(request, 'cautela_arma/cautela_edit.html', {'form': form, 'cautela': cautela})


@login_required
def cautela_list(request):
    cautela_list = Cautela.objects.order_by("numeroserie")
    busca = request.GET.get('busca')
    if busca:
        cautela_list = Cautela.objects.order_by("datacautela").filter(datacautela__icontains=busca) | \
            Cautela.objects.order_by("numerosgpe").filter(numerosgpe__icontains=busca) | \
            Cautela.objects.order_by("responsavel").filter(responsavel__icontains=busca) | \
            Cautela.objects.order_by("numeroserie").filter(numeroserie__icontains=busca) | \
            Cautela.objects.order_by("datadevolucao").filter(datadevolucao__icontains=busca) | \
            Cautela.objects.order_by("servidor").filter(servidor__icontains=busca) | \
            Cautela.objects.order_by("unidade").filter(unidade__icontains=busca)

    paginator = Paginator(cautela_list, 25)

    page = request.GET.get('page')
    cautelas = paginator.get_page(page)
    return render(request, 'cautela_arma/cautela_list.html', {'cautelas': cautelas})


@login_required
def cautela_arma(request):
    cautela = get_object_or_404(Cautela, pk=pk)
    unidades = Unidade.objects.all()
    servidores = Servidor.objects.all()
    form = CautelaFormCautela(instance=cautela)
    if request.method == 'POST':

        unidades = Unidade.objects.all()

        servidores = Servidor.objects.all()

        form = CautelaFormUpdate(request.POST, instance=cautela)

        if form.is_valid():
            cautela = form.save(commit=False)
            cautela.save()
            return redirect('/cautela_arma/list')
        else:
            return render(request, 'cautela_arma/cautela_arma.html', {'form': form, 'cautela': cautela,
                                                                      'unidades': unidades, 'servidores': servidores})
    elif request.method == 'GET':
        return render(request, 'cautela_arma/cautela_arma.html', {'form': form, 'cautela': cautela,
                                                                  'unidades': unidades, 'servidores': servidores})


@login_required
def cautela_nova(request):
    if request.method == 'GET':
        unidades = Unidade.objects.all()
        print(unidades)
        servidores = Servidor.objects.all()  
        print(servidores)
        armas = Arma.objects.all()
        print(armas)
        return render(request, 'cautela_arma/cautela_nova.html', {'unidades': unidades, 'servidores': servidores,
                                                                  'armas': armas})
    elif request.method == 'POST':
        datacautela = request.POST.get('datacautela')
        numerosgpe = request.POST.get('numerosgpe')
        responsavel = request.POST.get('responsavel')
        numeroserie = request.POST.get('numeroserie')
        servidor = request.POST.get('servidor')
        unidade = request.POST.get('unidade')

        return render(request, 'cautela_arma/cautela_nova.html', {'unidades': unidades, 'servidores': servidores,
                                                                  'armas': armas})


@login_required
def servidor(request):
    id_servidor = request.POST.get('id_servidor')
    servidor2 = Servidor.objects.filter(id=id_servidor)
    servidor_json = json.loads(serializers.serialize('json', servidor2))[0]['fields']
    print(servidor_json)
    return JsonResponse(servidor_json)


@login_required
def arma(request):
    id_arma = request.POST.get('id_arma')
    arma2 = Arma.objects.filter(id=id_arma)
    arma_json = json.loads(serializers.serialize('json', arma2))[0]['fields']
    print(arma_json)
    return JsonResponse(arma_json)

