from django.views.generic.edit import CreateView
from .models import Material, Projetil, Municao
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import MaterialFormUpdate
from django.core.paginator import Paginator


@method_decorator(login_required, name='dispatch')
class MaterialCreate(CreateView):
    model = Material
    fields = [
        'iis',
        'serie',
        'especie',
        'modelo',
        'fabricante',
        'material',
        'cor',
        'altura',
        'largura',
        'pesoliquido',
        'pesobruto',
        'retardo',
        'duploestagio',
        'unidade',
        'datacautela',
        'datatroca',
        'sgpecautela',
        'sgpetroca',
        'situacao',
    ]


@login_required
def material_edit(request, pk):
    material = get_object_or_404(Material, pk=pk)
    form = MaterialFormUpdate(instance=material)
    if request.method == 'POST':
        form = MaterialFormUpdate(request.POST, instance=material)

        if (form.is_valid()):
            material = form.save(commit=False)
            material.save()
            return redirect('/material/list')
        else:
            return render(request, 'material/material_edit.html', {'form': form, 'material': material})
    elif (request.method == 'GET'):
        return render(request, 'material/material_edit.html', {'form': form, 'material': material})


@login_required
def material_list(request):
    material_list = Material.objects.order_by("serie")
    busca = request.GET.get('busca')
    if busca:
        material_list = Material.objects.order_by("serie").filter(serie__icontains=busca) | \
            Material.objects.order_by("especie").filter(especie__icontains=busca) | \
            Material.objects.order_by("modelo").filter(modelo__icontains=busca) | \
            Material.objects.order_by("unidade").filter(unidade__nome__icontains=busca)

    paginator = Paginator(material_list, 15)

    page = request.GET.get('page')
    materials = paginator.get_page(page)
    return render(request, 'material/material_list.html', {'materials': materials})

@login_required
def material_tabela(request):
    material_tabela = Material.objects.order_by("serie")
    paginator = Paginator(material_tabela, 20000)

    page = request.GET.get('page')
    materials = paginator.get_page(page)
    return render(request, 'material/material_tabela.html', {'materials': materials})


@login_required
def projetil_tabela(request):
    projetil_tabela = Projetil.objects.order_by("modelo")
    paginator = Paginator(projetil_tabela, 200)

    page = request.GET.get('page')
    projetils = paginator.get_page(page)
    return render(request, 'material/projetil_tabela.html', {'projetils': projetils})

