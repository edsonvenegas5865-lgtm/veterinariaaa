# Sistema de Gestion para Clinica Veterinaria

Sistema web desarrollado con Python, Django, SQLite y Bootstrap 5.

## Funcionalidades

- Paginas publicas: Inicio, Acerca de Nosotros, Ubicacion, Contactos y Login.
- Autenticacion con usuarios de Django.
- Panel privado protegido.
- CRUD de Mascotas.
- CRUD de Enfermedades.
- Administracion desde Django Admin.

## Instalacion local

```powershell
cd C:\Users\veneg\OneDrive\Documentos\veterinaria\veterinariaaa
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Si PowerShell bloquea el entorno virtual:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\.venv\Scripts\Activate.ps1
```

## Rutas principales

- Publica: `http://127.0.0.1:8000/`
- Login: `http://127.0.0.1:8000/login/`
- Panel: `http://127.0.0.1:8000/panel/`
- Mascotas: `http://127.0.0.1:8000/mascotas/`
- Enfermedades: `http://127.0.0.1:8000/enfermedades/`
- Admin: `http://127.0.0.1:8000/admin/`

## Comandos utiles

```powershell
python manage.py createsuperuser
python manage.py test
python manage.py check
```
