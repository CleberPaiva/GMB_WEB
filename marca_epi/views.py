from django.views.generic.edit import CreateView
from .models import MarcaEpi
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import MarcaEpiFormUpdate
from django.core.paginator import Paginator


@method_decorator(login_required, name='dispatch')
class MarcaEpiCreate(CreateView):
    model = MarcaEpi
    fields = [
        'marcaEpi',
    ]


@login_required
def marca_epi_list(request):
    marca_epi_list = MarcaEpi.objects.order_by("marcaEpi")

    paginator = Paginator(marca_epi_list, 10)

    page = request.GET.get('page')
    marca_epis = paginator.get_page(page)
    return render(request, 'marca_epi/marcaEpi_list.html', {'marca_epis': marca_epis})


@login_required
def marca_epi_edit(request, pk):
    marca_epi = get_object_or_404(MarcaEpi, pk=pk)
    form = MarcaEpiFormUpdate(instance=marca_epi)
    if request.method == 'POST':
        form = MarcaEpiFormUpdate(request.POST, instance=marca_epi)

        if (form.is_valid()):
            marca_epi = form.save(commit=False)
            marca_epi.save()
            return redirect('/marca_epi/list')
        else:
            return render(request, 'marca_epi/marca_arma_edit.html', {'form': form, 'marca_epis': marca_epi})
    elif (request.method == 'GET'):
        return render(request, 'marca_epi/marca_epi_edit.html', {'form': form, 'marca_epis': marca_epi})


@login_required
def marca_epi_list(request):
    marca_epi_list = MarcaEpi.objects.order_by("marcaEpi")
    busca = request.GET.get('busca')
    if busca:
        marca_epi_list = MarcaEpi.objects.order_by("marcaEpi").filter(marcaEpi__icontains=busca)

    paginator = Paginator(marca_epi_list, 5)

    page = request.GET.get('page')
    marca_epis = paginator.get_page(page)
    return render(request, 'marca_epis/marca_arma_list.html', {'marca_epis': marca_epis})

@login_required
def marca_epi_tabela(request):
    marca_epi_tabela = MarcaEpi.objects.order_by("marcaEpi")
    paginator = Paginator(marca_epi_tabela, 100)

    page = request.GET.get('page')
    marca_epis = paginator.get_page(page)
    return render(request, 'marca_epi/marca_epi_tabela.html', {'marca_epis': marca_epis})


