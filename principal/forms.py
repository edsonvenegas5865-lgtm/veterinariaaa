from django import forms
from django.core.validators import RegexValidator

from .models import Enfermedad, Mascota


telefono_validator = RegexValidator(
    regex=r'^[0-9+\-\s]{7,20}$',
    message='Ingresa un telefono valido. Usa solo numeros, espacios, + o -.',
)


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
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Max'}),
            'especie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Perro'}),
            'raza': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Labrador'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'propietario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del propietario'}),
            'telefono_propietario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 099 999 9999'}),
        }
        error_messages = {
            'nombre': {'required': 'El nombre de la mascota es obligatorio.'},
            'especie': {'required': 'La especie es obligatoria.'},
            'edad': {'required': 'La edad es obligatoria.'},
            'propietario': {'required': 'El propietario es obligatorio.'},
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip()
        if len(nombre) < 2:
            raise forms.ValidationError('El nombre debe tener al menos 2 caracteres.')
        return nombre

    def clean_especie(self):
        especie = self.cleaned_data['especie'].strip()
        if len(especie) < 2:
            raise forms.ValidationError('La especie debe tener al menos 2 caracteres.')
        return especie

    def clean_edad(self):
        edad = self.cleaned_data['edad']
        if edad > 80:
            raise forms.ValidationError('La edad ingresada parece demasiado alta.')
        return edad

    def clean_raza(self):
        return self.cleaned_data.get('raza', '').strip()

    def clean_propietario(self):
        propietario = self.cleaned_data['propietario'].strip()
        if len(propietario) < 3:
            raise forms.ValidationError('El propietario debe tener al menos 3 caracteres.')
        return propietario

    def clean_telefono_propietario(self):
        telefono = self.cleaned_data.get('telefono_propietario', '').strip()
        if telefono:
            telefono_validator(telefono)
        return telefono


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
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Dermatitis'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripcion general'}),
            'sintomas': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Sintomas principales'}),
            'tratamiento': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Tratamiento recomendado'}),
        }
        error_messages = {
            'nombre': {'required': 'El nombre de la enfermedad es obligatorio.'},
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip()
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres.')
        return nombre

    def clean_descripcion(self):
        return self.cleaned_data.get('descripcion', '').strip()

    def clean_sintomas(self):
        return self.cleaned_data.get('sintomas', '').strip()

    def clean_tratamiento(self):
        return self.cleaned_data.get('tratamiento', '').strip()
