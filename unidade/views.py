from django.views.generic.edit import CreateView
from .models import Unidade
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UnidadeFormUpdate
from django.core.paginator import Paginator


@method_decorator(login_required, name='dispatch')
class UnidadeCreate(CreateView):
    model = Unidade
    fields = ['nome', 'telefone', 'email', 'endereco', 'gestor', 'orgao']


@login_required
def edit_unidade(request, pk):
    unidade = get_object_or_404(Unidade, pk=pk)
    form = UnidadeFormUpdate(instance=unidade)
    if request.method == 'POST':
        form = UnidadeFormUpdate(request.POST, instance=unidade)

        if (form.is_valid()):
            unidade = form.save(commit=False)
            #unidade.observacao = form.cleaned_data['observacao']
            unidade.save()
            return redirect('/unidade/list')
        else:
            return render(request, 'unidade/edit_unidade.html', {'form': form, 'unidade': unidade})
    elif (request.method == 'GET'):
        return render(request, 'unidade/edit_unidade.html', {'form': form, 'unidade': unidade})


@login_required
def unidade_list(request):
    unidade_list = Unidade.objects.order_by("nome")
    busca = request.GET.get('busca')
    if busca:
        unidade_list = Unidade.objects.order_by("nome").filter(nome__icontains=busca) | \
            Unidade.objects.order_by("nome").filter(gestor__icontains=busca) | \
            Unidade.objects.order_by("nome").filter(orgao__icontains=busca)

    paginator = Paginator(unidade_list, 10)

    page = request.GET.get('page')
    unidades = paginator.get_page(page)
    return render(request, 'unidade/unidade_list.html', {'unidades': unidades})
