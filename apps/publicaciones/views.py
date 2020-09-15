from django.shortcuts import render

# Create your views here.

def publicar(request):
    return render(request,"publicaciones/publicaciones.html")