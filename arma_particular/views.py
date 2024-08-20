from django.views.generic.edit import CreateView
from .models import ArmaParticular
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import ArmaParticularFormUpdate
from .forms import ArmaParticularFormCautela
from .forms import ArmaParticularForm
from django.core.paginator import Paginator
from unidade.models import Unidade
from django.http import JsonResponse


@method_decorator(login_required, name='dispatch')
class ArmaParticularCreate(CreateView):
    model = ArmaParticular
    fields = [
        'numeroserie',
        'nome',
        'cpf',
        'rg',
        'numerosigma',
        'numerosinarm',
        'numeroregistro',
        'amparo',
        'tipo',
        'marca',
        'calibre',
        'dataexpedicao',
        'datavalidade',
        'imagem',
        'imagem2',
        'imagem3',
    ]
    template_name = 'arma_particular/add_arma_particular.html'


@login_required
def arma_particular_edit(request, pk):
    armaparticular = get_object_or_404(ArmaParticular, pk=pk)
    form = ArmaParticularFormUpdate(instance=armaparticular)
    if request.method == 'POST':
        form = ArmaParticularFormUpdate(request.POST, instance=armaparticular)

        if form.is_valid():
            armaparticular = form.save(commit=False)
            armaparticular.save()
            return redirect('/arma_pparticular/list')
        else:
            return render(request, 'arma_particular/list_arma_particular.html', {'form': form, 'armaparticular': armaparticular})
    elif request.method == 'GET':
        return render(request, 'arma_particular/list_arma_particular.html', {'form': form, 'armaparticular': armaparticular})


@login_required
def arma_particular_list(request):
    arma_particular_list = ArmaParticular.objects.order_by("numeroserie")
    busca = request.GET.get('busca')

    if busca:
        arma_particular_list = ArmaParticular.objects.filter(numeroserie__icontains=busca) | \
            ArmaParticular.objects.filter(numerosigma__icontains=busca) | \
            ArmaParticular.objects.filter(numerosinarm__icontains=busca) | \
            ArmaParticular.objects.filter(calibre__icontains=busca) | \
            ArmaParticular.objects.filter(amparo__icontains=busca) | \
            ArmaParticular.objects.filter(nome__icontains=busca)

    paginator = Paginator(arma_particular_list, 10)

    page = request.GET.get('page')
    armasparticular = paginator.get_page(page)
    return render(request, 'arma_particular/list_arma_particular.html', {'armasparticular': armasparticular})