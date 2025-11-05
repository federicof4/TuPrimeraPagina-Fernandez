from django.urls import path
from . import views

app_name = 'turnos'

urlpatterns = [
    path('', views.TurnoListView.as_view(), name='turno_list'),
    path('nuevo/', views.TurnoCreateView.as_view(), name='turno_create'),
    path('<int:pk>/editar/', views.TurnoUpdateView.as_view(), name='turno_update'),
    path('<int:pk>/eliminar/', views.TurnoDeleteView.as_view(), name='turno_delete'),
]
