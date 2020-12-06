from django.db import models

# Create your models here.


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    categoria = models.CharField(max_length=50, null=True)
    imagen = models.ImageField(upload_to='productos', null=True)

    def __str__(self):
        return self.nombre

