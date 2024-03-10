from django.http import HttpResponse
from django.shortcuts import render

from .models import Cargo, Funcionario


def index(request):
    funcionarios = Funcionario.objects.order_by("nascimento")
    context = {"funcionarios": funcionarios}
    return render(request, "teste/index.html", context)


def cargos(request):
    cargos = Cargo.objects.all()
    context = {"cargos": cargos}
    return render(request, "teste/cargos.html", context)
