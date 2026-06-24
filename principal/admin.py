from django.contrib import admin

from .models import Enfermedad, Mascota


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'raza', 'propietario', 'telefono_propietario')
    search_fields = ('nombre', 'especie', 'raza', 'propietario')
    list_filter = ('especie',)


@admin.register(Enfermedad)
class EnfermedadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_registro')
    search_fields = ('nombre', 'descripcion', 'sintomas')
