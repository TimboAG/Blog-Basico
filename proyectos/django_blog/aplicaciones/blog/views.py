from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def general(request):
    return render(request, "general.html")

def cienciaficcion(request):
    return render(request, "cienciaficcion.html")

def tecnologia(request):
    return render(request, "tecnologia.html")

def programacion(request):
    return render(request, "programacion.html")

def videojuegos(request):
    return render(request, "videojuegos.html")

