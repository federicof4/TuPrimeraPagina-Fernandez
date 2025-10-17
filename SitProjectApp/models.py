from django.db import models

# Create your models here.
# vehiculos
# servicios
# clientes

class Vehiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()  
    chasis_nro = models.CharField(max_length=17, unique=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio})"


class Servicio(models.Model):
    tipo_servicio = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo_servicio} - ${self.precio}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}"