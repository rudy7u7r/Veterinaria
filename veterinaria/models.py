from django.db import models


class Mascota(models.Model):
    nombre = models.CharField(max_length=255)
    especie = models.CharField(max_length=255)
    raza = models.CharField(max_length=255)
    edad = models.PositiveIntegerField(default=0)
    sexo = models.CharField(
        max_length=20,
        choices=[('MACHO', 'Macho'), ('HEMBRA', 'Hembra')],
        default='MACHO'
    )
    peso = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    nombre_dueño = models.CharField(max_length=255)
    telefono_dueño = models.CharField(max_length=20, blank=True, default='')

    def __str__(self):
        return f"{self.nombre} ({self.especie})"


class Cita(models.Model):
    ESTADO_CHOICE = [
        ('PENDIENTE', 'Pendiente'),
        ('ATENDIDA', 'Atendida'),
        ('CANCELADA', 'Cancelada'),
    ]

    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo_consulta = models.TextField()
    descripcion_mascota = models.TextField(blank=True, default='')
    detalle_caso = models.TextField(blank=True, default='')
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICE,
        default='PENDIENTE'
    )

    def __str__(self):
        return f"cita para {self.mascota.nombre} el {self.fecha} a las {self.hora}"

##modelo Mascota (nombre, especie, raza, nombre dueño)

# Cita (mascota vinculada, fecha, hora, motivo de consulta, estado: pendiente/atendida/cancelada)