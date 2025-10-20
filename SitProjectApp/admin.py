from django.contrib import admin

# Register your models here.

from .models import Vehiculo, Servicio, Cliente

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'anio', 'chasis_nro', 'fecha_de_creacion')
    search_fields = ('marca', 'modelo', 'chasis_nro')
    ordering = ('fecha_de_creacion',)
    list_filter = ('anio', 'chasis_nro',)

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('tipo_servicio', 'precio', 'fecha_de_creacion')
    search_fields = ('tipo_servicio',)
    ordering = ('precio',)
    list_filter = ('precio',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'fecha_de_creacion')
    search_fields = ('nombre', 'apellido', 'email')
    ordering = ('apellido', 'nombre',)
    list_filter = ('fecha_de_creacion', 'apellido',)

