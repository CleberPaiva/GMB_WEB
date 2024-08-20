from django.views.generic.edit import CreateView
from .models import MarcaMunicao
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import MarcaMunicaoFormUpdate
from django.core.paginator import Paginator


@method_decorator(login_required, name='dispatch')
class MarcaMunicaoCreate(CreateView):
    model = MarcaMunicao
    fields = [
        'marcaMunicao',
    ]


@login_required
def marca_municao_list(request):
    marca_municao_list = MarcaMunicao.objects.order_by("marcaMunicao")

    paginator = Paginator(marca_municao_list, 10)

    page = request.GET.get('page')
    marca_municaos = paginator.get_page(page)
    return render(request, 'marca_municao/marcaMunicao_list.html', {'marca_municaos': marca_municaos})


@login_required
def marca_municao_edit(request, pk):
    marca_municao = get_object_or_404(MarcaMunicao, pk=pk)
    form = MarcaMunicaoFormUpdate(instance=marca_municao)
    if request.method == 'POST':
        form = MarcaMunicaoFormUpdate(request.POST, instance=marca_municao)

        if (form.is_valid()):
            marca_municao = form.save(commit=False)
            marca_municao.save()
            return redirect('/marca_municao/list')
        else:
            return render(request, 'marca_municao/marca_municao_edit.html', {'form': form, 'marca_municaos': marca_municao})
    elif (request.method == 'GET'):
        return render(request, 'marca_municao/marca_municao_edit.html', {'form': form, 'marca_municaos': marca_municao})


@login_required
def marca_municao_list(request):
    marca_municao_list = MarcaMunicao.objects.order_by("marcaMunicao")
    busca = request.GET.get('busca')
    if busca:
        marca_municao_list = MarcaMunicao.objects.order_by("marcaMunicao").filter(marcaMunicao__icontains=busca)

    paginator = Paginator(marca_municao_list, 5)

    page = request.GET.get('page')
    marca_municaos = paginator.get_page(page)
    return render(request, 'marca_municaos/marca_municao_list.html', {'marca_municaos': marca_municaos})


@login_required
def marca_municao_tabela(request):
    marca_municao_tabela = MarcaMunicao.objects.order_by("marcaMunicao")
    paginator = Paginator(marca_municao_tabela, 100)

    page = request.GET.get('page')
    marca_municaos = paginator.get_page(page)
    return render(request, 'marca_municao/marca_municao_tabela.html', {'marca_municaos': marca_municaos})