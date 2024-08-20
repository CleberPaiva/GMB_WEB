from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import MaterialCautelaTotal, CautelaMaterialTotal
from .models import Material
from django.http import JsonResponse
from .forms import MaterialTotalForm
from .forms import MaterialCautelaTotalForm



def adicionar_cautela(request):
    if request.method == 'POST':
            data_cautela = request.POST.get('data_cautela')
            unidade = request.POST.get('unidade')
            responsavel = request.POST.get('responsavel')
            matricula = request.POST.get('matricula')
            sgpe = request.POST.get('sgpe')
            material_gerals = request.POST.getlist('material_geral')
            cautela_materials = request.POST.getlist('cautela_material')
            series = request.POST.getlist('serie ')
            especies = request.POST.getlist('especie')
            modelos = request.POST.getlist('modelo')
            fabricantes = request.POST.getlist('fabricante')
            observacaos = request.POST.getlist('observacao')
            quantidades = request.POST.getlist('quantidade')

            # Salve o objeto CautelaMaterial
            cautelamaterial = CautelaMaterialTotal(
                data_cautela = data_cautela,
                unidade = unidade,
                responsavel = responsavel,
                matricula = matricula,
                sgpe = sgpe        
            )
            cautelamaterial.save()

            for material_geral, cautela_material, serie, especie, modelo, fabricante, observacao, quantidade in zip (material_gerals, cautela_materials, series, especies, modelos, fabricantes, observacaos, quantidades):
                materialcautela = MaterialCautelaTotal(material_geral=material_geral, cautela_material=cautela_material, serie=serie, especie=especie, modelo=modelo, fabricante=fabricante, observacao=observacao, quantidade=quantidade)
                materialcautela.save()

            return render(request, 'material_cautela/material_cautela.html')
     
    else:
        return render(request, 'material_cautela/material_cautela.html')


@login_required  # Adicione o decorador para exigir que o usuário esteja logado
def add_cautela_material_total(request):
    if request.method == 'POST':
        form = MaterialTotalForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)  # Não salve o formulário ainda
            material.save()  # Salve o registro no banco de dados
            return redirect('lista_material_cautela')  # Redireciona para a view 'arma_list' após salvar os dados
    else:
        form = MaterialTotalForm()

    return render(request, 'material_cautela/add_cautela_material_total.html', {'form': form})        


def add_material_total_form(request):
    form = MaterialCautelaTotalForm()
    return render(request, 'material_cautela/lista_material_cautela.html', {'form': form})


def add_material_total_save(request):
    form = MaterialCautelaTotalForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'errors': form.errors})    


@login_required
def material_info(request):
    material_id = request.GET.get('material_id', None)
    data = {'serie': '', 'especie': '', 'modelo': '', 'fabricante': ''}
        
    if material_id:
        try:
            material = Material.objects.get(id=material_id)
            data = {
                'serie': material.serie,
                'especie': material.especie,
                'modelo': material.modelo,
                'fabricante': material.fabricante,
            }
            print(data)  # Mostrar os dados no console
        except Material.DoesNotExist:
            pass
            
    return JsonResponse(data)


@login_required
def lista_material_cautela(request):
    cautela_material_list = CautelaMaterialTotal.objects.order_by('-data_cautela')
    material_cautela_list = MaterialCautelaTotal.objects.all()

    context = {
        'cautela_material_list': cautela_material_list,
        'material_cautela_list': material_cautela_list,
    }
    return render(request, 'material_cautela/lista_material_cautela.html', context)

def exibe_cautela(request, pk):
    cautela = get_object_or_404(CautelaMaterialTotal, pk=pk)
    material = MaterialCautelaTotal.objects.all()
    
    return render(request, 'material_cautela/exibe_cautela.html', {'cautela': cautela, 'material': material})

@login_required
def add_material(request, pk):
    cautela_material = get_object_or_404(CautelaMaterialTotal, pk=pk)
    materiais = Material.objects.all().order_by('iis')
    if request.method == 'POST':
        form = MaterialCautelaTotalForm(request.POST, request.POST)
        if form.is_valid():
            material = form.save(commit=False)
            cautela_material_id = request.POST.get('cautela_material')
            cautela_material = CautelaMaterialTotal.objects.get(id=cautela_material_id)
            material.cautela_material = cautela_material
            material.save()
            return redirect('lista_material_cautela')
    else:
        form = MaterialCautelaTotalForm()
        
    return render(request, 'material_cautela/add_material.html', {'form': form, 'cautela_material': cautela_material, 'materiais': materiais, 'pk': pk})


@login_required
def material_detail(request):
    material_id = request.GET.get('material_id', None)
    data = {'serie': '', 'especie': '', 'modelo': '', 'fabricante': ''}

    if material_id:
        try:
            material = Material.objects.get(pk=material_id)
            data = {
                'serie': material.serie,
                'especie': material.especie,
                'modelo': material.modelo,
                'fabricante': material.fabricante
            }
        except Material.DoesNotExist:
            pass     

    return JsonResponse(data)

@login_required
def cautela_material_imprime(request, pk):
    cautela = get_object_or_404(CautelaMaterialTotal, pk=pk)
    material = MaterialCautelaTotal.objects.all()
    first_name = request.user.first_name  # Acessa o primeiro nome do usuário

    return render(request, 'material_cautela/imprime_cautela.html', {'cautela': cautela, 'material': material, 'first_name': first_name})