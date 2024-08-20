from django.views.generic.edit import CreateView
from .models import Restricoes
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import RestricoesFormUpdate, RestricoesFormCautela
from django.core.paginator import Paginator
from django.urls import reverse_lazy


@method_decorator(login_required, name='dispatch')
class RestricoesCreate(CreateView):
    model = Restricoes
    fields = [
        'serie', 'patrimonio', 'especie', 'marca', 'modelo',
        'servidor', 'matricula', 'lotacao', 'sgperecebimento', 
        'situacao', 'tipo', 'atualizacao', 'motivo',
        'responsavelcadastramento', 'datacadastramento', 'obsevacoes',
    ]

    def get_success_url(self):
        return reverse_lazy('restricoes_tabela')


@login_required
def restricoes_edit(request, pk):
    restricoes = get_object_or_404(Restricoes, pk=pk)
    form = RestricoesFormUpdate(instance=restricoes)
    if request.method == 'POST':
        form = RestricoesFormUpdate(request.POST, instance=restricoes)

        if (form.is_valid()):
            restricoes = form.save(commit=False)
            restricoes.save()
            return redirect('/restricoes/tabela')
        else:
            return render(request, 'restricoes/restricoes_edit.html', {'form': form, 'restricoes': restricoes})
    elif (request.method == 'GET'):
        return render(request, 'restricoes/restricoes_edit.html', {'form': form, 'restricoes': restricoes})


@login_required
def restricoes_list(request):
    restricoes_list = Restricoes.objects.order_by("serie")
    busca = request.GET.get('busca')
    if busca:
        restricoes_list = Restricoes.objects.order_by("serie").filter(serie__icontains=busca) | \
            Restricoes.objects.order_by("patrimonio").filter(patrimonio__icontains=busca)

    paginator = Paginator(restricoes_list, 15)

    page = request.GET.get('page')
    restricoess = paginator.get_page(page)
    return render(request, 'restricoes/restricoes_list.html', {'restricoess': restricoess})


@login_required
def restricoes_tabela(request):
    restricoes_tabela = Restricoes.objects.order_by("serie")
    paginator = Paginator(restricoes_tabela, 10000)

    page = request.GET.get('page')
    restricoess = paginator.get_page(page)
    return render(request, 'restricoes/restricoes_tabela.html', {'restricoess': restricoess})


@login_required
def restricoes_cautela(request, pk):
    restricoes = get_object_or_404(Restricoes, pk=pk)
    form = RestricoesFormCautela(instance=restricoes)
    if request.method == 'POST':
        form = RestricoesFormCautela(request.POST, instance=restricoes)

        if (form.is_valid()):
            restricoes = form.save(commit=False)
            restricoes.save()
            return redirect('/restricoes/tabela')
        else:
            return render(request, 'restricoes/restricoes_cautela.html', {'form': form, 'restricoes': restricoes})
    elif (request.method == 'GET'):
        return render(request, 'restricoes/restricoes_cautela.html', {'form': form, 'restricoes': restricoes})


@login_required
def restricoes_cautela_imprime(request, pk):
    restricoes = get_object_or_404(Restricoes, pk=pk)
    form = RestricoesFormCautela(instance=restricoes)
    if request.method == 'POST':
        form = RestricoesFormCautela(request.POST, instance=restricoes)

        if (form.is_valid()):
            restricoes = form.save(commit=False)
            restricoes.save()
            return redirect('restricoes_cautela.html')
        else:
            return render(request, 'restricoes/restricoes_cautela_imprime.html', {'form': form, 'restricoes': restricoes})
    elif (request.method == 'GET'):
        return render(request, 'restricoes/restricoes_cautela_imprime.html', {'form': form, 'restricoes': restricoes})


@login_required
def restricoes_devolucao(request, pk):
    restricoes = get_object_or_404(Restricoes, pk=pk)
    form = RestricoesFormCautela(instance=restricoes)
    if request.method == 'POST':
        form = RestricoesFormCautela(request.POST, instance=restricoes)

        if (form.is_valid()):
            restricoes = form.save(commit=False)
            restricoes.save()
            return redirect('restricoes_cautela.html')
        else:
            return render(request, 'restricoes/restricoes_devolucao.html', {'form': form, 'restricoes': restricoes})
    elif (request.method == 'GET'):
        return render(request, 'restricoes/restricoes_devolucao.html', {'form': form, 'restricoes': restricoes})

@login_required
def restricoes_index(request):
    return render(request, 'restricoes/restricoes_index.html')


@login_required
def restricoes_aula(request):
    return render(request, 'restricoes/restricoes_aula.html')