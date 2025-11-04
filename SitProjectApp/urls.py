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
    path('vehiculo/detail/<int:pk>/', vehiculo_detail, name='vehiculo_detail'),
    path('vehiculo/edit/<int:pk>/', vehiculo_edit, name='vehiculo_edit'),
    path('vehiculo/delete/<int:pk>/', vehiculo_delete, name='vehiculo_delete'),
    
    path('servicio/detail/<int:pk>/', servicio_detail, name='servicio_detail'),
    path('servicio/edit/<int:pk>/', servicio_edit, name='servicio_edit'),
    path('servicio/delete/<int:pk>/', servicio_delete, name='servicio_delete'),

    path('cliente/detail/<int:pk>/', cliente_detail, name='cliente_detail'),
    path('cliente/edit/<int:pk>/', cliente_edit, name='cliente_edit'),
    path('cliente/delete/<int:pk>/', cliente_delete, name='cliente_delete'),
    
]