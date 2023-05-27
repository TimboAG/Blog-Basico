from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):    
    post= Post.objects.filter(activo=True)
    return render(request, "index.html",  {"post": post})

def general(request):
    post= Post.objects.filter(activo=True, categoria = Categoria.objects.get(nombre__iexact="General"))
    return render(request, "general.html",{"post": post})

def cienciaficcion(request):
    post= Post.objects.filter(activo=True, categoria = Categoria.objects.get(nombre__iexact="Ciencia Ficcion"))
    return render(request, "cienciaficcion.html", {"post": post})

def tecnologia(request):
    post= Post.objects.filter(activo=True, categoria = Categoria.objects.get(nombre__iexact="Tecnologia"))
    return render(request, "tecnologia.html", {"post": post})

def programacion(request):
    post= Post.objects.filter(activo=True, categoria = Categoria.objects.get(nombre__iexact="programacion"))
    return render(request, "programacion.html", {"post": post})

def videojuegos(request):
    post= Post.objects.filter(activo=True, categoria = Categoria.objects.get(nombre="Video juegos"))
    return render(request, "videojuegos.html", {"post": post})

def postdetalle(request, slug):
    # post= Post.objects.get(slug =slug) 
    post = get_object_or_404(Post, slug =slug)
    return render(request, "post.html", {"postdetalle": post})  
  
