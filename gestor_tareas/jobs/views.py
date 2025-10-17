from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Tarea

# vista tareas (lista tareas, detalles tarea, crear tarea, actualizar tarea, eliminar tarea) con protectores de vistas y autenticacion de usuarios, detalle, creación y edición deben abrirse en modales en lista de tareas

@login_required
def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'lista_tareas.html', {'tareas': tareas})

@login_required
def detalle_tarea(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    return render(request, 'templates/lista_tarea.html', {'tarea': tarea})

@login_required
def crear_tarea(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        tarea = Tarea(titulo=titulo, descripcion=descripcion)
        tarea.save()
        return redirect('lista_tareas')
    return render(request, 'templates/lista_tareas.html')

@login_required
def actualizar_tarea(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    if request.method == 'POST':
        tarea.titulo = request.POST['titulo']
        tarea.descripcion = request.POST['descripcion']
        tarea.completada = 'completada' in request.POST
        tarea.save()
        return redirect('lista_tareas')
    return render(request, 'templates/modal_lista_tarea.html', {'tarea': tarea})

@login_required
def eliminar_tarea(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    if request.method == 'POST':
        tarea.delete()
        return redirect('lista_tareas')
    return render(request, 'lista_tareas.html', {'tarea': tarea})

#lista de templates necesarios:
# lista_tareas.html (para listar tareas y modales para detalles, creación y edición)
# modal_detalle_tarea.html (modal para detalles de tarea)
# modal_crear_tarea.html (modal para crear tarea)
# modal_actualizar_tarea.html (modal para actualizar tarea)