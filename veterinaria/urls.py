from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_diario_citas, name='home'),
    path('citas-diarias/', views.listado_diario_citas, name='listado_diario'),
    path('agendar-cita/', views.agendar_cita, name='agendar_cita'),
    path('registrar-mascota/', views.registrar_mascota, name='registrar_mascota'),
    path('historial-clinico/', views.historial_clinico, name='historial_clinico'),
]
