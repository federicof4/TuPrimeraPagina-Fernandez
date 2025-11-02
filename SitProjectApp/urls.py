from django.urls import path
from .views import *

app_name = 'SitProjectApp'

urlpatterns = [
    path('', index,name='index'),   
    path('servicio/create/', servicio_create, name='servicio_create'),
    path('cliente/create/', cliente_create, name='cliente_create'),
    path('vehiculo/create/', vehiculo_create, name='vehiculo_create'),
    path('servicio/list/', servicio_list, name='servicio_list'),
    path('cliente/list/', cliente_list, name='cliente_list'),
    path('vehiculo/list/', vehiculo_list, name='vehiculo_list'),
    path('about/', about, name='about'),
]