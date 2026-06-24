from django.contrib import admin

from .models import Mascota


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'raza', 'propietario', 'telefono_propietario')
    search_fields = ('nombre', 'especie', 'raza', 'propietario')
    list_filter = ('especie',)
