from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, 'principal/inicio.html')


def acerca(request):
    return render(request, 'principal/acerca.html')


def ubicacion(request):
    return render(request, 'principal/ubicacion.html')


def contactos(request):
    return render(request, 'principal/contactos.html')


@login_required
def panel(request):
    return render(request, 'principal/panel.html')
