from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acerca/', views.acerca, name='acerca'),
    path('ubicacion/', views.ubicacion, name='ubicacion'),
    path('contactos/', views.contactos, name='contactos'),
    path('login/', auth_views.LoginView.as_view(template_name='principal/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('panel/', views.panel, name='panel'),
    path('mascotas/', views.mascotas, name='mascotas'),
    path('mascotas/crear/', views.crear_mascota, name='crear_mascota'),
    path('mascotas/<int:mascota_id>/editar/', views.editar_mascota, name='editar_mascota'),
    path('mascotas/<int:mascota_id>/eliminar/', views.eliminar_mascota, name='eliminar_mascota'),
    path('enfermedades/', views.enfermedades, name='enfermedades'),
    path('enfermedades/crear/', views.crear_enfermedad, name='crear_enfermedad'),
    path('enfermedades/<int:enfermedad_id>/editar/', views.editar_enfermedad, name='editar_enfermedad'),
    path('enfermedades/<int:enfermedad_id>/eliminar/', views.eliminar_enfermedad, name='eliminar_enfermedad'),
]
