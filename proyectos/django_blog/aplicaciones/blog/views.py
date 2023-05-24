from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):    
    post= Post.objects.filter(activo=True)
    return render(request, "index.html",  {"post": post})

def general(request):
    post= Post.objects.filter(activo=True, categoria = Categoria.objects.get(nombre="General"))
    return render(request, "general.html",{"post": post})

def cienciaficcion(request):
    post= Post.objects.filter(activo=True, categoria = Categoria.objects.get(nombre="Ciencia Ficcion"))
    return render(request, "cienciaficcion.html", {"post": post})

def tecnologia(request):
    post= Post.objects.filter(activo=True, categoria = Categoria.objects.get(nombre="Tecnologia"))
    return render(request, "tecnologia.html", {"post": post})

def programacion(request):
    post= Post.objects.filter(activo=True, categoria = Categoria.objects.get(nombre="Programacion"))
    return render(request, "programacion.html", {"post": post})

def videojuegos(request):
    post= Post.objects.filter(activo=True, categoria = Categoria.objects.get(nombre="Video juegos"))
    return render(request, "videojuegos.html", {"post": post})

