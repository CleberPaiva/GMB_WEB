from django.views.generic.edit import CreateView
from .models import Pessoa
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import PessoaFormUpdate
from django.core.paginator import Paginator
from django.contrib.auth.models import User


@method_decorator(login_required, name='dispatch')
class PessoaCreate(CreateView):
    model = Pessoa
    fields = [
        'nome',
        'user',
        'unidade',
        'matricula',
        'cpf',
        'endereco',
        'telefone',
        'email',
        'funcao',
        'cidade'
    ]


@login_required
def pessoa_edit(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    form = PessoaFormUpdate(instance=pessoa)
    if request.method == 'POST':
        form = PessoaFormUpdate(request.POST, instance=pessoa)

        if (form.is_valid()):
            pessoa = form.save(commit=False)
            pessoa.save()
            return redirect('/pessoa/list')
        else:
            return render(request, 'pessoa/pessoa_edit.html', {'form': form, 'pessoa': pessoa})
    elif (request.method == 'GET'):
        return render(request, 'pessoa/pessoa_edit.html', {'form': form, 'pessoa': pessoa})


@login_required
def pessoa_list(request):
    pessoa_list = Pessoa.objects.order_by("nome")
    busca = request.GET.get('busca')
    if busca:
        pessoa_list = Pessoa.objects.order_by("nome").filter(nome__icontains=busca) | \
            Pessoa.objects.order_by("matricula").filter(matricula__icontains=busca)

    paginator = Paginator(pessoa_list, 5)

    page = request.GET.get('page')
    pessoas = paginator.get_page(page)
    return render(request, 'pessoa/pessoa_list.html', {'pessoas': pessoas})

