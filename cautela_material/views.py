from django.shortcuts import render, redirect
from .forms import CautelaMaterialForm
from .models import Material, CautelaMaterial
from django.http import JsonResponse


def add_cautela(request):
    print(request.POST)
    if request.method == 'POST':
        form = CautelaMaterialForm(request.POST)
        if form.is_valid():
            material = form.cleaned_data.get('material_geral')
            quantity = form.cleaned_data.get('quantidade')

            # Verifique se a quantidade do material é suficiente
            if material.quantidade >= quantity:
                # Atualize a quantidade no model Material
                material.quantidade -= quantity
                material.save()

                # Salve o objeto CautelaMaterial
                cautela = form.save(commit=False) 
                cautela.quantidade = quantity
                cautela.save()

                return redirect('home')
            else:
                form.add_error('quantidade', 'Quantidade excede a disponibilidade do material.') 
    else:
        form = CautelaMaterialForm()

    return render(request, 'cautela_material/cautela_material.html', {'form': form})


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
        except Material.DoesNotExist:
            pass
        
    return JsonResponse(data)