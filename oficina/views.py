from django.views.generic.edit import CreateView
from .models import Oficina
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import OficinaFormUpdate
from django.core.paginator import Paginator
from unidade.models import Unidade


@method_decorator(login_required, name='dispatch')
class OficinaCreate(CreateView):
    model = Oficina
    fields = [
        'dataentrada',
        'datasaida',
        'numeroseria',
        'especie',
        'modelo',
        'cargapara',
        'unidade',
        'historico',
        'servico',
        'usuario'
    ]


@login_required
def oficina_edit(request, pk):
    oficina = get_object_or_404(Oficina, pk=pk)
    form = OficinaFormUpdate(instance=oficina)
    if request.method == 'POST':
        form = OficinaFormUpdate(request.POST, instance=oficina)

        if (form.is_valid()):
            oficina = form.save(commit=False)
            oficina.save()
            return redirect('/oficina/tabela')
        else:
            return render(request, 'oficina/oficina_edit.html', {'form': form, 'oficina': oficina})
    elif (request.method == 'GET'):
        return render(request, 'oficina/oficina_edit.html', {'form': form, 'oficina': oficina})


@login_required
def oficina_list(request):
    oficina_list = Oficina.objects.order_by("numeroseria")
    busca = request.GET.get('busca')
    if busca:
        oficina_list = Oficina.objects.order_by("numeroseria").filter(numeroseria__icontains=busca) | \
            Oficina.objects.order_by("numeroseria").filter(modelo__icontains=busca)

    paginator = Paginator(oficina_list, 5)

    page = request.GET.get('page')
    oficinas = paginator.get_page(page)
    return render(request, 'oficina/oficina_list.html', {'oficinas': oficinas})

@login_required
def oficina_tabela(request):
    oficina_tabela = Oficina.objects.order_by("numeroseria")
    paginator = Paginator(oficina_tabela, 100)

    page = request.GET.get('page')
    oficinas = paginator.get_page(page)
    return render(request, 'oficina/oficina_tabela.html', {'oficinas': oficinas})


@login_required
def unidade_list(request):
    unidades = Unidade.objects.all().order_by("nome")
    return render(request, 'unidade/unidade_list.html', {'unidades': unidades})
