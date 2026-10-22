from datetime import time
from django.shortcuts import render, redirect
from .models import Cita, Mascota
from django.utils.timezone import localdate


def listado_diario_citas(request):
    hoy = localdate()
    citas_hoy = Cita.objects.filter(fecha=hoy).order_by('hora')

    total_citas = Cita.objects.count()
    urgencias = Cita.objects.filter(estado='PENDIENTE').count()
    pacientes = Mascota.objects.count()

    context = {
        'citas': citas_hoy,
        'hoy': hoy,
        'total_citas': total_citas,
        'urgencias': urgencias,
        'pacientes': pacientes,
    }
    return render(request, 'veterinaria/listado_diario.html', context)


def registrar_mascota(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        especie = request.POST.get('especie')
        raza = request.POST.get('raza')
        edad = request.POST.get('edad')
        sexo = request.POST.get('sexo')
        peso = request.POST.get('peso')
        nombre_dueño = request.POST.get('nombre_dueño')
        telefono_dueño = request.POST.get('telefono_dueño')
        descripcion_mascota = request.POST.get('descripcion_mascota', '')
        motivo_consulta = request.POST.get('motivo_consulta', '')
        detalle_caso = request.POST.get('detalle_caso', motivo_consulta)
        fecha = request.POST.get('fecha') or str(localdate())
        hora = request.POST.get('hora') or '09:00'

        mascota = Mascota.objects.create(
            nombre=nombre,
            especie=especie,
            raza=raza,
            edad=int(edad or 0),
            sexo=sexo,
            peso=peso or 0,
            nombre_dueño=nombre_dueño,
            telefono_dueño=telefono_dueño or ''
        )

        Cita.objects.create(
            mascota=mascota,
            fecha=localdate() if not fecha else fecha,
            hora=time.fromisoformat(hora),
            motivo_consulta=motivo_consulta,
            descripcion_mascota=descripcion_mascota,
            detalle_caso=detalle_caso,
            estado='PENDIENTE'
        )
        return redirect('listado_diario')
    return render(request, 'veterinaria/registrar_mascota.html')


def historial_clinico(request):
    citas = Cita.objects.select_related('mascota').order_by('-fecha', '-hora')
    return render(request, 'veterinaria/historial_clinico.html', {'citas': citas})


def agendar_cita(request):
    mascotas = Mascota.objects.order_by('nombre')

    if request.method == 'POST':
        ya_registrado = request.POST.get('ya_registrado') == 'on'

        if ya_registrado:
            mascota_id = request.POST.get('mascota_existente')
            mascota = Mascota.objects.get(id=mascota_id)
            motivo_consulta = request.POST.get('motivo_consulta', '')
            detalle_caso = request.POST.get('detalle_caso', motivo_consulta)
            fecha = request.POST.get('fecha') or str(localdate())
            hora = request.POST.get('hora') or '09:00'
            descripcion_mascota = request.POST.get('descripcion_mascota', '')

            Cita.objects.create(
                mascota=mascota,
                fecha=fecha,
                hora=time.fromisoformat(hora),
                motivo_consulta=motivo_consulta,
                descripcion_mascota=descripcion_mascota,
                detalle_caso=detalle_caso,
                estado='PENDIENTE'
            )
            return redirect('listado_diario')

        nombre = request.POST.get('nombre')
        especie = request.POST.get('especie')
        raza = request.POST.get('raza')
        edad = request.POST.get('edad')
        sexo = request.POST.get('sexo')
        peso = request.POST.get('peso')
        nombre_dueño = request.POST.get('nombre_dueño')
        telefono_dueño = request.POST.get('telefono_dueño')
        descripcion_mascota = request.POST.get('descripcion_mascota', '')
        motivo_consulta = request.POST.get('motivo_consulta', '')
        detalle_caso = request.POST.get('detalle_caso', motivo_consulta)
        fecha = request.POST.get('fecha') or str(localdate())
        hora = request.POST.get('hora') or '09:00'

        mascota = Mascota.objects.create(
            nombre=nombre,
            especie=especie,
            raza=raza,
            edad=int(edad or 0),
            sexo=sexo,
            peso=peso or 0,
            nombre_dueño=nombre_dueño,
            telefono_dueño=telefono_dueño or '',
        )

        Cita.objects.create(
            mascota=mascota,
            fecha=fecha,
            hora=time.fromisoformat(hora),
            motivo_consulta=motivo_consulta,
            descripcion_mascota=descripcion_mascota,
            detalle_caso=detalle_caso,
            estado='PENDIENTE'
        )
        return redirect('listado_diario')

    return render(request, 'veterinaria/agendar_cita.html', {'mascotas': mascotas})