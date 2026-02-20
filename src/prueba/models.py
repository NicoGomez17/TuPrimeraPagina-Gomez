from django.db import models

# Create your models here.

from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()

