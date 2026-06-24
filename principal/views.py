from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .forms import EnfermedadForm, MascotaForm
from .models import Enfermedad, Mascota


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


@login_required
def editar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)

    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('mascotas')
    else:
        form = MascotaForm(instance=mascota)

    return render(request, 'principal/mascota_form.html', {'form': form, 'mascota': mascota})


@login_required
def eliminar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)

    if request.method == 'POST':
        mascota.delete()
        return redirect('mascotas')

    return render(request, 'principal/mascota_confirmar_eliminar.html', {'mascota': mascota})


@login_required
def enfermedades(request):
    enfermedades_registradas = Enfermedad.objects.all().order_by('nombre')
    return render(
        request,
        'principal/enfermedades.html',
        {'enfermedades': enfermedades_registradas},
    )


@login_required
def crear_enfermedad(request):
    if request.method == 'POST':
        form = EnfermedadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enfermedades')
    else:
        form = EnfermedadForm()

    return render(request, 'principal/enfermedad_form.html', {'form': form})


@login_required
def editar_enfermedad(request, enfermedad_id):
    enfermedad = get_object_or_404(Enfermedad, id=enfermedad_id)

    if request.method == 'POST':
        form = EnfermedadForm(request.POST, instance=enfermedad)
        if form.is_valid():
            form.save()
            return redirect('enfermedades')
    else:
        form = EnfermedadForm(instance=enfermedad)

    return render(
        request,
        'principal/enfermedad_form.html',
        {'form': form, 'enfermedad': enfermedad},
    )


@login_required
def eliminar_enfermedad(request, enfermedad_id):
    enfermedad = get_object_or_404(Enfermedad, id=enfermedad_id)

    if request.method == 'POST':
        enfermedad.delete()
        return redirect('enfermedades')

    return render(
        request,
        'principal/enfermedad_confirmar_eliminar.html',
        {'enfermedad': enfermedad},
    )
