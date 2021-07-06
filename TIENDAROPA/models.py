from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import FloatField
from datetime import datetime

# Create your models here.

class Categoria(models.Model):
    descripcionCategoria = models.CharField(max_length=150)

class Producto(models.Model):
    titulo = models.CharField(max_length=60) 
    img= models.BinaryField(null=True)
    mimetype = models.CharField(max_length=150, null=True)
    name = models.CharField(max_length=150, null=True)
    descripcionProducto = models.CharField(max_length=150)  
    precio = models.FloatField() 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False)
    fecha = models.DateTimeField(default=datetime.now)

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    productos = models.ManyToManyField(Producto)
    total = FloatField()





    
    