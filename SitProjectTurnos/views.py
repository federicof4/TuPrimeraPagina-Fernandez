from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Turno


class TurnoListView(LoginRequiredMixin, ListView):
    model = Turno
    template_name = 'SitProjectTurnos/turno_list.html'
    context_object_name = 'turnos'


class TurnoCreateView(LoginRequiredMixin, CreateView):
    model = Turno
    fields = ['fecha', 'horas', 'vehiculo', 'servicio']
    template_name = 'SitProjectTurnos/turno_form.html'
    success_url = reverse_lazy('turnos:turno_list')


class TurnoUpdateView(LoginRequiredMixin, UpdateView):
    model = Turno
    fields = ['fecha', 'horas', 'vehiculo', 'servicio']
    template_name = 'SitProjectTurnos/turno_form.html'
    success_url = reverse_lazy('turnos:turno_list')


class TurnoDeleteView(LoginRequiredMixin, DeleteView):
    model = Turno
    template_name = 'SitProjectTurnos/turno_confirm_delete.html'
    success_url = reverse_lazy('turnos:turno_list')

