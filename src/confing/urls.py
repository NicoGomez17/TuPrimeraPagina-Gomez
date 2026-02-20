"""
URL configuration for confing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from prueba.views import inicio, crear_autor, crear_categoria, crear_post, buscar_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="Inicio"),
    path('autor-nuevo/', crear_autor, name="AutorNuevo"),
    path('categoria-nueva/', crear_categoria, name="CategoriaNueva"),
    path('post-nuevo/', crear_post, name="PostNuevo"),
    path('buscar/', buscar_post, name="Buscar"),
]

