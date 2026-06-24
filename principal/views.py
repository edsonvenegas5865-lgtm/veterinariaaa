from django.http import HttpResponse


def inicio(request):
    return HttpResponse('Sistema de Gestion Veterinaria')
