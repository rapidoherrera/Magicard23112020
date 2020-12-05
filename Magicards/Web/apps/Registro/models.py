from django.core.checks.messages import Info
from django.db import models

# Create your models here.
class Cuenta(models.Model):
    alias = models.CharField(max_length=20)
    edad = models.CharField(max_length=2)
    descripcion = models.TextField(max_length=50)

    def __str__(self):
        return self.alias

class Info(models.Model):
    cuenta = models.ForeignKey(Cuenta, null=True, blank=True, on_delete=models.CASCADE)
    rut = models.CharField(max_length=9)
    nombre = models.CharField(max_length=10)
    apellido_paterno = models.CharField(max_length=10)
    apellido_materno = models.CharField(max_length=10)
    telefono = models.CharField(max_length=20)
    domicilio = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now=True)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

