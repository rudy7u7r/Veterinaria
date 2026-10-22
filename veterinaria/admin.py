from django.contrib import admin
from .models import Mascota, Cita


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'raza', 'nombre_dueño')
    search_fields = ('nombre', 'nombre_dueño')
    
@admin.register(Cita)
class  CitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'mascota', 'fecha', 'hora', 'estado')
    
    list_filters = ('fecha', 'estado')
    
    search_fields = ('mascota_nombre', 'motivo_consulta')
    
    list_editable = ('estado',)
# Register your models here.
