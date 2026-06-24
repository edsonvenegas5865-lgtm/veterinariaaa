from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .forms import EnfermedadForm, MascotaForm
from .models import Enfermedad, Mascota


class VistasPrivadasTests(TestCase):
    def test_mascotas_requiere_login(self):
        response = self.client.get(reverse('mascotas'))

        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response['Location'])

    def test_enfermedades_requiere_login(self):
        response = self.client.get(reverse('enfermedades'))

        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response['Location'])

    def test_usuario_autenticado_ve_listado_mascotas(self):
        User.objects.create_user(username='admin', password='admin12345')
        self.client.login(username='admin', password='admin12345')

        response = self.client.get(reverse('mascotas'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Mascotas')


class FormulariosTests(TestCase):
    def test_formulario_mascota_valido(self):
        form = MascotaForm(data={
            'nombre': 'Luna',
            'especie': 'Canino',
            'raza': 'Criolla',
            'edad': 4,
            'propietario': 'Ana Perez',
            'telefono_propietario': '3001234567',
        })

        self.assertTrue(form.is_valid())

    def test_formulario_mascota_rechaza_edad_alta(self):
        form = MascotaForm(data={
            'nombre': 'Luna',
            'especie': 'Canino',
            'raza': 'Criolla',
            'edad': 120,
            'propietario': 'Ana Perez',
            'telefono_propietario': '3001234567',
        })

        self.assertFalse(form.is_valid())

    def test_formulario_enfermedad_valido(self):
        form = EnfermedadForm(data={
            'nombre': 'Dermatitis',
            'descripcion': 'Irritacion de la piel',
            'sintomas': 'Picazon',
            'tratamiento': 'Control veterinario',
        })

        self.assertTrue(form.is_valid())


class ModelosTests(TestCase):
    def test_crear_mascota(self):
        mascota = Mascota.objects.create(
            nombre='Milo',
            especie='Felino',
            raza='Criollo',
            edad=2,
            propietario='Carlos Ruiz',
        )

        self.assertEqual(str(mascota), 'Milo')

    def test_crear_enfermedad(self):
        enfermedad = Enfermedad.objects.create(nombre='Otitis')

        self.assertEqual(str(enfermedad), 'Otitis')

# Create your tests here.
