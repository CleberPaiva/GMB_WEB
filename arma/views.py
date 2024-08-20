from django.views.generic.edit import CreateView
from .models import Arma
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import ArmaFormUpdate
from .forms import ArmaFormCautela
from .forms import ArmaForm
from django.core.paginator import Paginator
from unidade.models import Unidade
from pessoa.models import Pessoa
from django.http import JsonResponse


@method_decorator(login_required, name='dispatch')
class ArmaCreate(CreateView):
    model = Arma
    fields = [
        'numeroserie',
        'cnpj',
        'numeropatri',
        'numerosinarm',
        'especie',
        'marca',
        'modelo',
        'calibre',
        'capacidade',
        'qtcarregador',
        'funcionamento',
        'acabamento',
        'qtcanos',
        'compricanos',
        'tipoalma',
        'qtraias',
        'sentidorais',
        'paisfabricacao',
        'acessorios',
        'docregistro',
        'tipomunicao',
        'datacompra',
        'unidade',
        'servidor',
    ]


@login_required
def arma_edit(request, pk):
    arma = get_object_or_404(Arma, pk=pk)
    form = ArmaFormUpdate(instance=arma)
    if request.method == 'POST':
        form = ArmaFormUpdate(request.POST, instance=arma)

        if form.is_valid():
            arma = form.save(commit=False)
            arma.save()
            return redirect('/arma/list')
        else:
            return render(request, 'arma/arma_edit.html', {'form': form, 'arma': arma})
    elif request.method == 'GET':
        return render(request, 'arma/arma_edit.html', {'form': form, 'arma': arma})


@login_required
def arma_list(request):
    busca = request.GET.get('busca')
    unidades = Unidade.objects.all()

    if busca is not None:
        arma_list = Arma.objects.filter(numeroserie__icontains=busca).order_by("numeroserie") | \
            Arma.objects.filter(unidade__icontains=busca) | \
            Arma.objects.filter(numeropatri__icontains=busca) | \
            Arma.objects.filter(especie__icontains=busca) | \
            Arma.objects.filter(matricula__icontains=busca) | \
            Arma.objects.filter(modelo__icontains=busca) | \
            Arma.objects.filter(servidor__icontains=busca)
    else:
        arma_list = Arma.objects.all()

    paginator = Paginator(arma_list, 10)

    page = request.GET.get('page')
    armas = paginator.get_page(page)
    return render(request, 'arma/arma_list.html', {'armas': armas, 'unidades': unidades})


@login_required
def arma_tabela(request):
    arma_tabela = Arma.objects.order_by("numeroserie")
    paginator = Paginator(arma_tabela, 8200)

    page = request.GET.get('page')
    armas = paginator.get_page(page)
    return render(request, 'arma/arma_tabela.html', {'armas': armas})



@login_required
def arma_cautela(request, pk):
    arma = get_object_or_404(Arma, pk=pk)
    unidades = Unidade.objects.all()
    servidores = Pessoa.objects.all().order_by('matricula')
    form = ArmaFormCautela(request.POST or None, instance=arma)
    if request.method == 'POST':
        form = ArmaFormCautela(request.POST, instance=arma)

        if form.is_valid():
            arma = form.save(commit=False)
            arma.save()
            return redirect('arma_cautela_imprime', pk=arma.pk)
        else:
            return render(request, 'arma/arma_cautela.html', {'form': form, 'arma': arma, 'unidades': unidades, 'servidores': servidores})
    elif request.method == 'GET':
        return render(request, 'arma/arma_cautela.html', {'form': form, 'arma': arma, 'unidades': unidades, 'servidores': servidores})


@login_required
def arma_cautela_imprime(request, pk):
    arma = get_object_or_404(Arma, pk=pk)
    form = ArmaFormCautela(instance=arma)
    if request.method == 'POST':
        form = ArmaFormCautela(request.POST, instance=arma)

        if (form.is_valid()):
            arma = form.save(commit=False)
            arma.save()
            return redirect('arma_cautela.html')
        else:
            return render(request, 'arma/arma_cautela_imprime.html', {'form': form, 'arma': arma})
    elif (request.method == 'GET'):
        return render(request, 'arma/arma_cautela_imprime.html', {'form': form, 'arma': arma})


@login_required
def arma_devolucao(request, pk):
    arma = get_object_or_404(Arma, pk=pk)
    form = ArmaFormCautela(instance=arma)
    if request.method == 'POST':
        form = ArmaFormCautela(request.POST, instance=arma)

        if (form.is_valid()):
            arma = form.save(commit=False)
            arma.save()
            return redirect('arma_cautela.html')
        else:
            return render(request, 'arma/arma_devolucao.html', {'form': form, 'arma': arma})
    elif (request.method == 'GET'):
        return render(request, 'arma/arma_devolucao.html', {'form': form, 'arma': arma})


@login_required  # Adicione o decorador para exigir que o usuário esteja logado
def add_arma(request):
    if request.method == 'POST':
        form = ArmaForm(request.POST, request.FILES)
        if form.is_valid():
            arma = form.save(commit=False)  # Não salve o formulário ainda
            arma.usuario = request.user  # Associe o usuário logado ao registro
            arma.save()  # Salve o registro no banco de dados
            return redirect('arma_list')  # Redireciona para a view 'arma_list' após salvar os dados
    else:
        form = ArmaForm()

    return render(request, 'arma/add_arma.html', {'form': form})


@login_required
def edit_arma(request, pk):
    arma = get_object_or_404(Arma, pk=pk)
    unidades = Unidade.objects.all()
    form = ArmaFormCautela(instance=arma)
    if request.method == 'POST':
        unidades = Unidade.objects.all()
        form = ArmaFormCautela(request.POST, instance=arma)

        if form.is_valid():
            arma = form.save(commit=False)
            arma.save()
            return redirect('/arma/list')
        else:
            return render(request, 'arma/edit_arma.html', {'form': form, 'arma': arma, 'unidades': unidades})
    elif request.method == 'GET':
        return render(request, 'arma/edit_arma.html', {'form': form, 'arma': arma, 'unidades': unidades})


@login_required
def get_arma_details(request):
    arma_id = request.GET.get("arma_id")
    # print("Arma ID:", arma_id)
    if arma_id:
        arma = get_object_or_404(Arma, pk=arma_id)
        arma_data = {
            "numeroserie": arma.numeroserie,
            "numerosinarm": arma.numerosinarm,
            "numeropatri": arma.numeropatri,
            "marca": arma.marca,
            "modelo": arma.modelo,
            "calibre": arma.calibre,
            "capacidade": arma.capacidade,
            "qtcarregador": arma.qtcarregador,
            "qtmunicao": arma.qtmunicao,
            "acessorios": arma.acessorios,
            "tipomunicao": arma.tipomunicao,
            "gensmunicao": arma.gensmunicao,
            "unidade": arma.unidade,
            "servidor": arma.servidor,
            "matricula": arma.matricula,
            "telefone": arma.telefone,
            "datacautela": arma.datacautela,
            "numerosgpe": arma.numerosgpe,
            "observacoes": arma.observacoes,
            # Adicione outras informações, conforme necessário
        }
        return JsonResponse(arma_data)
    else:
        return JsonResponse({"error": "Invalid arma ID"})
