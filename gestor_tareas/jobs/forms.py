#formulario de tareas

from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'completada']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'completada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'titulo': 'Título',
            'descripcion': 'Descripción',
            'completada': 'Completada',
        }
        help_texts = {
            'titulo': 'Ingrese el título de la tarea',
            'descripcion': 'Ingrese una descripción de la tarea',
            'completada': 'Marque esta casilla si la tarea está completada',
        }
        error_messages = {
            'titulo': {
                'required': 'El título es obligatorio',
            },
        }
        # Puedes agregar validaciones personalizadas si es necesario
        def clean_titulo(self):
            titulo = self.cleaned_data.get('titulo')
            if 'tarea' not in titulo.lower():
                raise forms.ValidationError('El título debe contener la palabra "tarea"')
            return titulo
        def clean_descripcion(self):
            descripcion = self.cleaned_data.get('descripcion')
            if len(descripcion) < 10:
                raise forms.ValidationError('La descripción debe tener al menos 10 caracteres')
            return descripcion
        def clean(self):
            cleaned_data = super().clean()  
            titulo = cleaned_data.get('titulo')
            descripcion = cleaned_data.get('descripcion')
            if titulo and descripcion and titulo.lower() in descripcion.lower():
                raise forms.ValidationError('El título no debe estar contenido en la descripción')
            return cleaned_data
        