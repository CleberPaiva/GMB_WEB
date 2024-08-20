from django.views.generic.edit import CreateView
from .models import Fornecedor
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import FornecedorFormUpdate
from django.core.paginator import Paginator


@method_decorator(login_required, name='dispatch')
class FornecedorCreate(CreateView):
    model = Fornecedor
    fields = [
        'nomefantasia',
        'razaosocial',
        'endereco',
        'telefone',
        'email',
    ]


@login_required
def fornecedor_edit(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    form = FornecedorFormUpdate(instance=fornecedor)
    if request.method == 'POST':
        form = FornecedorFormUpdate(request.POST, instance=fornecedor)

        if (form.is_valid()):
            fornecedor = form.save(commit=False)
            fornecedor.save()
            return redirect('/fornecedor/list')
        else:
            return render(request, 'fornecedor/fornecedor_edit.html', {'form': form, 'fornecedor': fornecedor})
    elif (request.method == 'GET'):
        return render(request, 'fornecedor/fornecedor_edit.html', {'form': form, 'fornecedor': fornecedor})


@login_required
def fornecedor_list(request):
    fornecedor_list = Fornecedor.objects.order_by("nomefantasia")
    busca = request.GET.get('busca')
    if busca:
        fornecedor_list = Fornecedor.objects.order_by("nomefantasia").filter(nomefantasia__icontains=busca) | \
            Fornecedor.objects.order_by("razaosocial").filter(razaosocial__icontains=busca)

    paginator = Paginator(fornecedor_list, 5)

    page = request.GET.get('page')
    fornecedors = paginator.get_page(page)
    return render(request, 'fornecedor/fornecedor_list.html', {'fornecedors': fornecedors})
