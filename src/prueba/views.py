from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Autor, Categoria, Post

def inicio(request):
    return render(request, "prueba/base.html")

def crear_autor(request):
    if request.method == "POST":
        nuevo = Autor(
            nombre=request.POST['nombre'],
            email=request.POST['email'])
        nuevo.save()
        return render(request, "prueba/base.html")
    return render(request, "prueba/form_autor.html")

def crear_categoria(request):
    if request.method == "POST":
        nuevo = Categoria(nombre=request.POST['nombre'])
        nuevo.save()
        return render(request, "prueba/base.html")
    return render(request, "prueba/form_categoria.html")

def crear_post(request):
    if request.method == "POST":
        nuevo = Post(titulo=request.POST['titulo'], contenido=request.POST['contenido'])
        nuevo.save()
        return render(request, "prueba/base.html")
    return render(request, "prueba/form_post.html")

def buscar_post(request):
    if request.GET.get("titulo"):
        busqueda = request.GET["titulo"]
        resultados = Post.objects.filter(titulo__icontains=busqueda)
        return render(request, "prueba/buscar.html", {"posts": resultados})
    return render(request, "prueba/buscar.html")


