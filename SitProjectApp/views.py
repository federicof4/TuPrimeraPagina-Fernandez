from django.shortcuts import render, redirect
from .models import Servicio, Cliente, Vehiculo
from .forms import ServicioForm, ClienteForm, VehiculoForm


# Create your views here.
def index(request):
    return render(request, 'SitProjectApp/index.html')

def servicio_create(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SitProjectApp:servicio_list')
    else:
        form = ServicioForm()
    return render(request, 'SitProjectApp/servicio_create.html', {'form': form})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SitProjectApp:cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'SitProjectApp/cliente_create.html', {'form': form})

def vehiculo_create(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SitProjectApp:vehiculo_list')
    else:
        form = VehiculoForm()
    return render(request, 'SitProjectApp/vehiculo_create.html', {'form': form})

def servicio_list(request):
    query = request.GET.get('q', '')
    if len(query) > 0:
        servicio_list = Servicio.objects.filter(descripcion__icontains=query).order_by('fecha_de_creacion')
    else:
        servicio_list = Servicio.objects.all().order_by('fecha_de_creacion')

    context = {
        'servicio_list': servicio_list,
        'query': query,
    }
    return render(request, 'SitProjectApp/servicio_list.html', context)

def cliente_list(request):
    query = request.GET.get('q', '')
    if len(query) > 0:
        cliente_list = Cliente.objects.filter(nombre__icontains=query).order_by('apellido')
    else:
        cliente_list = Cliente.objects.all().order_by('apellido')
    context = {
        'cliente_list': cliente_list,
        'query': query,
    }    
    return render(request, 'SitProjectApp/cliente_list.html', context)

def vehiculo_list(request):
    query = request.GET.get('q', '')
    if len(query) > 0:
        vehiculo_list = Vehiculo.objects.filter(marca__icontains=query).order_by('modelo')
    else:
        vehiculo_list = Vehiculo.objects.all().order_by('modelo')
    context = {
        'vehiculo_list': vehiculo_list,
        'query': query,
    }
    return render(request, 'SitProjectApp/vehiculo_list.html', context)