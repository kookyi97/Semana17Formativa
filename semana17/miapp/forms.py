from django import forms
from .models import Autor, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'nacionalidad']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el apellido'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la nacionalidad'}),
        }
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido', 
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'nacionalidad': 'Nacionalidad',
        }

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha_publicacion', 'genero', 'isbn']
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el género'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el ISBN'}),
        }
        labels = {
            'titulo': 'Título',
            'autor': 'Autor',
            'fecha_publicacion': 'Fecha de Publicación',
            'genero': 'Género',
            'isbn': 'ISBN',
        }