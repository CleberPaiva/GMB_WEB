from django.views.generic.edit import CreateView
from .models import Municao
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import MunicaoFormUpdate
from .forms import MunicaoFormCautela
from .forms import MunicaoForm
from django.core.paginator import Paginator
from unidade.models import Unidade
from django.http import JsonResponse
from pessoa.models import Pessoa


@method_decorator(login_required, name='dispatch')
class MunicaoCreate(CreateView):
    model = Municao
    fields = [
        'gens',
        'calibre',
        'tipo',
        'marca',
        'quantidade',
        'nome',
        'matricula',
        'data',
        'sgpe',
        'responsavel',
        'unidade',
        'observacoes',
    ]
    template_name = 'municao/add_municao.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servidores'] = Pessoa.objects.all().order_by('matricula')
        return context


@login_required
def municao_edit(request, pk):
    municao = get_object_or_404(Municao, pk=pk)
    form = MunicaoFormUpdate(instance=municao)
    if request.method == 'POST':
        form = MunicaoFormUpdate(request.POST, instance=municao)

        if form.is_valid():
            municao = form.save(commit=False)
            municao.save()
            return redirect('/municao/list')
        else:
            return render(request, 'municao/list_municao.html', {'form': form, 'municao': municao})
    elif request.method == 'GET':
        return render(request, 'municao/list_municao.html', {'form': form, 'municao': municao})


@login_required
def municao_list(request):
    municao_list = Municao.objects.order_by("gens")
    busca = request.GET.get('busca')

    if busca:
        municao_list = Municao.objects.filter(nome__icontains=busca) | \
            Municao.objects.filter(unidade__icontains=busca) | \
            Municao.objects.filter(matricula__icontains=busca) | \
            Municao.objects.filter(responsavel__icontains=busca) | \
            Municao.objects.filter(sgpe__icontains=busca) | \
            Municao.objects.filter(tipo__icontains=busca) | \
            Municao.objects.filter(observacoes__icontains=busca) | \
            Municao.objects.filter(marca__icontains=busca) | \
            Municao.objects.filter(calibre__icontains=busca)

    paginator = Paginator(municao_list, 10)

    page = request.GET.get('page')
    municao = paginator.get_page(page)
    return render(request, 'municao/list_municao.html', {'municao': municao})


@login_required
def municao_imprime(request, pk):
    municao = get_object_or_404(Municao, pk=pk)
    form = MunicaoFormCautela(instance=municao)
    if request.method == 'POST':
        form = MunicaoFormCautela(request.POST, instance=municao)

        if form.is_valid():
            municao = form.save(commit=False)
            municao.save()
            return redirect('municao_list')
        else:
            return render(request, 'municao/municao_imprime.html', {'form': form, 'municao': municao})
    elif request.method == 'GET':
        return render(request, 'municao/municao_imprime.html', {'form': form, 'municao': municao})