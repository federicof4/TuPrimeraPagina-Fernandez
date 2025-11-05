from django.db import models
from django.contrib.auth.models import User
from SitProjectApp.models import Vehiculo, Servicio

class Turno(models.Model):
    fecha = models.DateField()
    horas = models.DecimalField(max_digits=4, decimal_places=2)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha']
        verbose_name_plural = "Turnos"

    def __str__(self):
        return f"Turno de {self.vehiculo} para {self.servicio} el {self.fecha}"

