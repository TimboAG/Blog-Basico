from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def general(request):
    return render(request, "general.html")

