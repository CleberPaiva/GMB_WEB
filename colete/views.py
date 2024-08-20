from django.views.generic.edit import CreateView
from .models import Colete
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import ColeteFormUpdate, ColeteFormCautela, ColeteForm
from django.core.paginator import Paginator
from unidade.models import Unidade
from servidor.models import Servidor
from django.http import JsonResponse


@method_decorator(login_required, name='dispatch')
class ColeteCreate(CreateView):
    model = Colete
    fields = [
        'numeroserie', 'cnpj', 'numeropatri', 'especie', 'pais', 'marca', 'nivel',
        'sexo', 'tamanho', 'modelo', 'lote', 'datafabricacao', 'garantia', 'capa', 'servidor', 'cargo',
        'unidade', 'sgpe', 'situacao', 'datacautela', 'atualizacao', 'historico', 'matricula', 'tipo', 'observacoes',
    ]


@login_required
def unidade_list(request):
    unidade_list = Unidade.objects.order_by("nome")

    paginator = Paginator(unidade_list, 10)

    page = request.GET.get('page')
    unidades = paginator.get_page(page)
    return render(request, 'unidade/unidade_list.html', {'unidades': unidades})


@login_required
def servidor_list(request):
    servidor_list = Servidor.objects.order_by("nome")

    paginator = Paginator(servidor_list, 10)

    page = request.GET.get('page')
    servidors = paginator.get_page(page)
    return render(request, 'servidor/servidor_list.html', {'servidors': servidors})


@login_required
def colete_edit(request, pk):
    colete = get_object_or_404(Colete, pk=pk)
    form = ColeteFormUpdate(instance=colete)
    if request.method == 'POST':
        form = ColeteFormUpdate(request.POST, instance=colete)

        if (form.is_valid()):
            colete = form.save(commit=False)
            colete.save()
            return redirect('/colete/list')
        else:
            return render(request, 'colete/colete_edit.html', {'form': form, 'colete': colete})
    elif (request.method == 'GET'):
        return render(request, 'colete/colete_edit.html', {'form': form, 'colete': colete})


@login_required
def colete_list(request):
    colete_list = Colete.objects.order_by("numeroserie")
    busca = request.GET.get('busca')
    if busca:
        colete_list = Colete.objects.order_by("numeroserie").filter(numeroserie__icontains=busca) | \
            Colete.objects.order_by("numeropatri").filter(numeropatri__icontains=busca) | \
            Colete.objects.order_by("servidor").filter(servidor__icontains=busca)

    paginator = Paginator(colete_list, 15)

    page = request.GET.get('page')
    coletes = paginator.get_page(page)
    return render(request, 'colete/colete_list.html', {'coletes': coletes})


@login_required
def colete_tabela(request):
    colete_tabela = Colete.objects.order_by("numeroserie")
    paginator = Paginator(colete_tabela, 10000)

    page = request.GET.get('page')
    coletes = paginator.get_page(page)
    return render(request, 'colete/colete_tabela.html', {'coletes': coletes})


@login_required
def colete_cautela(request, pk):
    colete = get_object_or_404(Colete, pk=pk)
    form = ColeteFormCautela(instance=colete)
    if request.method == 'POST':
        form = ColeteFormCautela(request.POST, instance=colete)

        if (form.is_valid()):
            colete = form.save(commit=False)
            colete.save()
            return redirect('/colete/list')
        else:
            return render(request, 'colete/colete_cautela.html', {'form': form, 'colete': colete})
    elif (request.method == 'GET'):
        return render(request, 'colete/colete_cautela.html', {'form': form, 'colete': colete})


@login_required
def colete_cautela_imprime(request, pk):
    colete = get_object_or_404(Colete, pk=pk)
    form = ColeteFormCautela(instance=colete)
    if request.method == 'POST':
        form = ColeteFormCautela(request.POST, instance=colete)

        if (form.is_valid()):
            colete = form.save(commit=False)
            colete.save()
            return redirect('colete_cautela.html')
        else:
            return render(request, 'colete/colete_cautela_imprime.html', {'form': form, 'colete': colete})
    elif (request.method == 'GET'):
        return render(request, 'colete/colete_cautela_imprime.html', {'form': form, 'colete': colete})


@login_required
def colete_devolucao(request, pk):
    colete = get_object_or_404(Colete, pk=pk)
    form = ColeteFormCautela(instance=colete)
    if request.method == 'POST':
        form = ColeteFormCautela(request.POST, instance=colete)

        if (form.is_valid()):
            colete = form.save(commit=False)
            colete.save()
            return redirect('colete_cautela.html')
        else:
            return render(request, 'colete/colete_devolucao.html', {'form': form, 'colete': colete})
    elif (request.method == 'GET'):
        return render(request, 'colete/colete_devolucao.html', {'form': form, 'colete': colete})


@login_required  # Adicione o decorador para exigir que o usuário esteja logado
def add_colete(request):
    if request.method == 'POST':
        form = ColeteForm(request.POST, request.FILES)
        if form.is_valid():
            colete = form.save(commit=False)  # Não salve o formulário ainda
            colete.usuario = request.user  # Associe o usuário logado ao registro
            colete.save()  # Salve o registro no banco de dados
            return redirect('colete_list') # Redireciona para a view 'colete_list' após salvar os dados
    else:
        form = ColeteForm()

    return render(request, 'colete/add_colete.html', {'form': form})


@login_required
def edit_colete(request, pk):
    colete = get_object_or_404(Colete, pk=pk)
    unidades = Unidade.objects.all()
    form = ColeteFormCautela(instance=colete)
    if request.method == 'POST':
        unidades = Unidade.objects.all()
        form = ColeteFormCautela(request.POST, instance=colete)

        if form.is_valid():
            colete = form.save(commit=False)
            colete.save()
            return redirect('/colete/list')
        else:
            return render(request, 'colete/edit_colete.html', {'form': form, 'colete': colete, 'unidades': unidades})
    elif request.method == 'GET':
        return render(request, 'colete/edit_colete.html', {'form': form, 'colete': colete, 'unidades': unidades})


@login_required
def get_colete_details(request):
    colete_id = request.GET.get("colete_id")
    #  print("Colete ID:", colete_id)
    if colete_id:
        colete = get_object_or_404(Colete, pk=colete_id)
        colete_data = {
            "numeroserie": colete.numeroserie,
            "numeropatri": colete.numeropatri,
            "marca": colete.marca,
            "especie": colete.especie,
            "nivel": colete.nivel,
            "modelo": colete.modelo,
            "tamanho": colete.tamanho,
            "unidade": colete.unidade,
            "servidor": colete.servidor,
            "matricula": colete.matricula,
            "cargo": colete.cargo,
            "datafabricacao": colete.datafabricacao,
            "garantia": colete.garantia,
            "capa": colete.capa,
            "sgpe": colete.sgpe,
            "datacautela": colete.datacautela,
            "tipo": colete.tipo,
            "observacoes": colete.observacoes,
            # Adicione outras informações, conforme necessário
        }
        return JsonResponse(colete_data)
    else:
        return JsonResponse({"error": "Invalid colete ID"})


