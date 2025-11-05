from django.contrib import admin
from .models import Turno

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'horas', 'vehiculo', 'servicio', 'fecha_creacion')
    list_filter = ('fecha', 'vehiculo', 'servicio')
    search_fields = ('vehiculo__placa', 'servicio__nombre')
    ordering = ('-fecha',)
