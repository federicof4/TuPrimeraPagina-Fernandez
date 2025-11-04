from django.shortcuts import render, redirect
from .models import Servicio, Cliente, Vehiculo
from .forms import ServicioForm, ClienteForm, VehiculoForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'SitProjectApp/index.html')

def about(request):
    return render(request, 'SitProjectApp/about.html')

@login_required
def servicio_create(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SitProjectApp:servicio_list')
    else:
        form = ServicioForm()
    return render(request, 'SitProjectApp/servicio_create.html', {'form': form})

@login_required
def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SitProjectApp:cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'SitProjectApp/cliente_create.html', {'form': form})

@login_required
def vehiculo_create(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SitProjectApp:vehiculo_list')
    else:
        form = VehiculoForm()
    return render(request, 'SitProjectApp/vehiculo_create.html', {'form': form})

@login_required
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

@login_required
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

@login_required
def vehiculo_list(request):
    query = request.GET.get('q', '')
    if len(query) > 0:
        vehiculo_list = Vehiculo.objects.filter(marca__icontains=query).order_by('id')
    else:
        vehiculo_list = Vehiculo.objects.all().order_by('id')
    context = {
        'vehiculo_list': vehiculo_list,
        'query': query,
    }
    return render(request, 'SitProjectApp/vehiculo_list.html', context)

@login_required
def vehiculo_detail(request, pk):
    vehiculo = Vehiculo.objects.get(pk=pk)
    return render(request, 'SitProjectApp/vehiculo_detail.html', {'vehiculo': vehiculo})

@login_required
def vehiculo_delete(request, pk):
    vehiculo = Vehiculo.objects.get(pk=pk)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('SitProjectApp:vehiculo_list')
    return render(request, 'SitProjectApp/vehiculo_delete.html', {'vehiculo': vehiculo})



@login_required
def vehiculo_edit(request, pk):
    vehiculo = Vehiculo.objects.get(pk=pk)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('SitProjectApp:vehiculo_list')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'SitProjectApp/vehiculo_edit.html', {'form': form})



@login_required
def servicio_edit(request, pk):
    servicio = Servicio.objects.get(pk=pk)
    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('SitProjectApp:servicio_list')
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'SitProjectApp/servicio_edit.html', {'form': form})



@login_required
def servicio_detail(request, pk):
    servicio = Servicio.objects.get(pk=pk)
    return render(request, 'SitProjectApp/servicio_detail.html', {'servicio': servicio})

@login_required
def servicio_delete(request, pk):
    servicio = Servicio.objects.get(pk=pk)
    if request.method == 'POST':
        servicio.delete()
        return redirect('SitProjectApp:servicio_list')
    return render(request, 'SitProjectApp/servicio_delete.html', {'servicio': servicio})

@login_required
def cliente_edit(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('SitProjectApp:cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'SitProjectApp/cliente_edit.html', {'form': form})


@login_required
def cliente_detail(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    return render(request, 'SitProjectApp/cliente_detail.html', {'cliente': cliente})

@login_required
def cliente_delete(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('SitProjectApp:cliente_list')
    return render(request, 'SitProjectApp/cliente_delete.html', {'cliente': cliente})
