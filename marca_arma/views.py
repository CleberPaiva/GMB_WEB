from django.views.generic.edit import CreateView
from .models import MarcaArma
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import MarcaArmaFormUpdate
from django.core.paginator import Paginator


@method_decorator(login_required, name='dispatch')
class MarcaArmaCreate(CreateView):
    model = MarcaArma
    fields = [
        'marcaArma',
    ]


@login_required
def marca_arma_list(request):
    marca_arma_list = MarcaArma.objects.order_by("marcaArma")

    paginator = Paginator(marca_arma_list, 10)

    page = request.GET.get('page')
    marca_armas = paginator.get_page(page)
    return render(request, 'marca_arma/marcaArma_list.html', {'marca_armas': marca_armas})


@login_required
def marca_arma_edit(request, pk):
    marca_arma = get_object_or_404(MarcaArma, pk=pk)
    form = MarcaArmaFormUpdate(instance=marca_arma)
    if request.method == 'POST':
        form = MarcaArmaFormUpdate(request.POST, instance=marca_arma)

        if (form.is_valid()):
            marca_arma = form.save(commit=False)
            marca_arma.save()
            return redirect('/marca_arma/list')
        else:
            return render(request, 'marca_arma/marca_arma_edit.html', {'form': form, 'marca_armas': marca_arma})
    elif (request.method == 'GET'):
        return render(request, 'marca_arma/marca_arma_edit.html', {'form': form, 'marca_armas': marca_arma})


@login_required
def marca_arma_list(request):
    marca_arma_list = MarcaArma.objects.order_by("marcaArma")
    busca = request.GET.get('busca')
    if busca:
        marca_arma_list = MarcaArma.objects.order_by("marcaArma").filter(marcaArma__icontains=busca)

    paginator = Paginator(marca_arma_list, 5)

    page = request.GET.get('page')
    marca_armas = paginator.get_page(page)
    return render(request, 'marca_arma/marca_arma_list.html', {'marca_armas': marca_armas})

@login_required
def marca_arma_tabela(request):
    marca_arma_tabela = MarcaArma.objects.order_by("marcaArma")
    paginator = Paginator(marca_arma_tabela, 100)

    page = request.GET.get('page')
    marca_armas = paginator.get_page(page)
    return render(request, 'marca_arma/marca_arma_tabela.html', {'marca_armas': marca_armas})


