from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Autor, Libro
from .forms import AutorForm, LibroForm

def home(request):
    return render(request, 'miapp/home.html', {
        'total_autores': Autor.objects.count(),
        'total_libros': Libro.objects.count(),
    })

class ListaAutoresView(ListView):
    model = Autor
    template_name = 'miapp/lista_autores.html'
    context_object_name = 'autores'
    
    def get_queryset(self):
        return Autor.objects.all().order_by('apellido', 'nombre')

class CrearAutorView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'miapp/crear_autor.html'
    success_url = reverse_lazy('miapp:lista_autores')
    
    def form_valid(self, form):
        messages.success(self.request, '¡Autor creado exitosamente!')
        return super().form_valid(form)

class ListaLibrosView(ListView):
    model = Libro
    template_name = 'miapp/lista_libros.html'
    context_object_name = 'libros'
    
    def get_queryset(self):
        return Libro.objects.all().select_related('autor').order_by('titulo')

class CrearLibroView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'miapp/crear_libro.html'
    success_url = reverse_lazy('miapp:lista_libros')
    
    def form_valid(self, form):
        messages.success(self.request, '¡Libro creado exitosamente!')
        return super().form_valid(form)