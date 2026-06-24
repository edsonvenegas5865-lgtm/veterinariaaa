from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acerca/', views.acerca, name='acerca'),
    path('ubicacion/', views.ubicacion, name='ubicacion'),
    path('contactos/', views.contactos, name='contactos'),
    path('login/', auth_views.LoginView.as_view(template_name='principal/login.html'), name='login'),
]
