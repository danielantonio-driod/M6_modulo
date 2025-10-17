# Gestor de Tareas Django

Este proyecto es una aplicación web para la gestión de tareas, desarrollada con Django. Permite crear, ver, actualizar y eliminar tareas usando una interfaz moderna y responsiva basada en Bootstrap, con operaciones en modales.

## Requisitos
- Python 3.8+
- Django 5+

## Instalación
1. Clona el repositorio o descarga el código.
2. Instala las dependencias en un entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # En Windows
   pip install django
   ```
3. Aplica las migraciones:
   ```bash
   python manage.py makemigrations jobs
   python manage.py migrate
   ```
4. (Opcional) Crea un superusuario para acceder al admin:
   ```bash
   python manage.py createsuperuser
   ```
5. Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```
6. Accede a la app en [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   admin temporal darri - 1234 

## Uso
- Desde la página principal puedes:
  - Crear nuevas tareas (botón "Crear Nueva Tarea")
  - Ver detalles, editar o eliminar tareas usando los botones correspondientes en la tabla
  - Todas las operaciones se realizan en modales para una mejor experiencia de usuario

## Estructura principal
- `jobs/` - App principal con modelos, vistas, formularios y templates
- `templates/` - Contiene los archivos HTML para la lista y los modales
- `tareas/` - Configuración global del proyecto

## Créditos
Desarrollado por d-labs.
