#urls para tareas
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('crear/', views.crear_tarea, name='crear_tarea'),
    path('<int:tarea_id>/', views.detalle_tarea, name='detalle_tarea'),
    path('<int:tarea_id>/actualizar/', views.actualizar_tarea, name='actualizar_tarea'),
    path('<int:tarea_id>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),
]
