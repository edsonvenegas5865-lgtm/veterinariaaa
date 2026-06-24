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

    def clean_propietario(self):
        propietario = self.cleaned_data['propietario'].strip()
        if len(propietario) < 3:
            raise forms.ValidationError('El propietario debe tener al menos 3 caracteres.')
        return propietario


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

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip()
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres.')
        return nombre
