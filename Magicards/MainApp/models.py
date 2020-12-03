from django.db import models
from django.utils import timezone

# Create your models here.

class Persona (models.Model):
    rut = models.CharField(max_length=10)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)  
    correo = models.EmailField(max_length=30, default='deprueba@gmail.com')
    direccion = models.CharField(max_length=30, default='direccion de prueba 123')
    telefono = models.CharField(max_length=11, default="12345678901" )
    fecha_creacion = models.DateTimeField(default=timezone.now)   
    
    # credencial uno por la pagina solo se pueden crear usuario clientes, los admin o funcionarios se crean desde admin directamente
    cred = models.IntegerField(default = 1)
    def __str__(self):
        return self.nombres   

# class Bicicleta (models.Model):
#     cod = models.IntegerField()
#     marca = models.CharField(max_length=30,default = 'shimano')
#     modelo = models.CharField(max_length=30, default = 'ETP-765')
#     is_disponible = models.BooleanField(default=True)
    
#     def __int__(self):
#         return self.cod

class Producto (models.Model):
    cod_prod = models.IntegerField()
    nom_prod = models.CharField(max_length=30)
    desc_prod = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    precio = models.IntegerField()
    stock = models.IntegerField()
    is_disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)   
    
    def __int__(self):
        return self.cod_prod