from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import MascotaForm
from .models import Mascota


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


@login_required
def mascotas(request):
    mascotas_registradas = Mascota.objects.all().order_by('nombre')
    return render(
        request,
        'principal/mascotas.html',
        {'mascotas': mascotas_registradas},
    )


@login_required
def crear_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mascotas')
    else:
        form = MascotaForm()

    return render(request, 'principal/mascota_form.html', {'form': form})
