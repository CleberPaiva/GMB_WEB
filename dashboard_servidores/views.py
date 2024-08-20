from django.http import JsonResponse
from django.shortcuts import render
from pessoa.models import Pessoa
from django.core import serializers


def dashboard_with_pivot_servidores(request):
    return render(request, 'dashboard_servidores/dashboard_with_pivot_servidores.html', {})


def pivot_data_servidores(request):
    dataset = Pessoa.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)
