from django import forms

from .models import Enfermedad, Mascota


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


class EnfermedadForm(forms.ModelForm):
    class Meta:
        model = Enfermedad
        fields = [
            'nombre',
            'descripcion',
            'sintomas',
            'tratamiento',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'sintomas': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tratamiento': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
