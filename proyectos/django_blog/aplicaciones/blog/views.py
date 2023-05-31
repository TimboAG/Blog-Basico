from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def home(request):    
    queryset= request.GET.get("buscar")
    post= Post.objects.filter(activo=True)
    if queryset:
        post= Post.objects.filter(Q(titulo__icontains = queryset ) | Q(descripcion__icontains = queryset )  ).distinct()
    
    paginator= Paginator(post,1)
    page=request.GET.get('page')
    post=paginator.get_page(page)
    return render(request, "index.html",  {"post": post})

def general(request):
    queryset= request.GET.get("buscar")
    post= Post.objects.filter(activo=True, categoria = Categoria.objects.get(nombre__iexact="General"))
    if queryset:
        post= Post.objects.filter(Q(titulo__icontains = queryset ) | Q(descripcion__icontains = queryset ),
                                activo=True, categoria = Categoria.objects.get(nombre__iexact="General")).distinct()
    paginator= Paginator(post,1)
    page=request.GET.get('page')
    post=paginator.get_page(page)
    return render(request, "general.html",{"post": post})

def cienciaficcion(request):
    queryset= request.GET.get("buscar")    
    post= Post.objects.filter(activo=True, categoria = Categoria.objects.get(nombre__iexact="Ciencia Ficcion"))
    if queryset:
        post= Post.objects.filter(Q(titulo__icontains = queryset ) | Q(descripcion__icontains = queryset ),
                                activo=True, categoria = Categoria.objects.get(nombre__iexact="Ciencia Ficcion")).distinct()
    paginator= Paginator(post,1)
    page=request.GET.get('page')
    post=paginator.get_page(page)
    return render(request, "cienciaficcion.html", {"post": post})

def tecnologia(request):
    queryset= request.GET.get("buscar")    
    post= Post.objects.filter(activo=True, categoria = Categoria.objects.get(nombre__iexact="Tecnologia"))
    if queryset:
            post= Post.objects.filter(Q(titulo__icontains = queryset ) | Q(descripcion__icontains = queryset ),
                                activo=True, categoria = Categoria.objects.get(nombre__iexact="Tecnologia")).distinct()
    paginator= Paginator(post,1)
    page=request.GET.get('page')
    post=paginator.get_page(page)
    return render(request, "tecnologia.html", {"post": post})

def programacion(request):
    queryset= request.GET.get("buscar")    
    post= Post.objects.filter(activo=True, categoria = Categoria.objects.get(nombre__iexact="programacion"))
    if queryset:
            post= Post.objects.filter(Q(titulo__icontains = queryset ) | Q(descripcion__icontains = queryset ),
                                activo=True, categoria = Categoria.objects.get(nombre__iexact="programacion")).distinct()
    return render(request, "programacion.html", {"post": post})

def videojuegos(request):
    queryset= request.GET.get("buscar")    
    post= Post.objects.filter(activo=True, categoria = Categoria.objects.get(nombre="Video juegos"))
    if queryset:
            post= Post.objects.filter(Q(titulo__icontains = queryset ) | Q(descripcion__icontains = queryset ),
                                activo=True, categoria = Categoria.objects.get(nombre__iexact="Video juegos")).distinct()
    paginator= Paginator(post,1)
    page=request.GET.get('page')
    post=paginator.get_page(page)
    return render(request, "videojuegos.html", {"post": post})

def postdetalle(request, slug):
    # post= Post.objects.get(slug =slug) 
    post = get_object_or_404(Post, slug =slug)
    return render(request, "post.html", {"postdetalle": post})    