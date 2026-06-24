from django import forms

from .models import Mascota


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = [
            'nombre',
            'especie',
            'raza',
            'edad',
            'propietario',
            'telefono_propietario',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'especie': forms.TextInput(attrs={'class': 'form-control'}),
            'raza': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'propietario': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_propietario': forms.TextInput(attrs={'class': 'form-control'}),
        }
