from django.http import JsonResponse
from django.shortcuts import render
from arma.models import Arma
from django.core import serializers


def dashboard_with_pivot(request):
    return render(request, 'dashboard/dashboard_with_pivot.html', {})


def pivot_data(request):
    dataset = Arma.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)