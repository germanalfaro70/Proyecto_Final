import csv
from django.conf import settings
from django.shortcuts import render
from .metricas import obtener_metricas_consumo
RUTA_CSV = settings.BASE_DIR / 'data' / 'registros_consumo.csv'

def cargar_registros_csv(ruta):
    with open(ruta, newline='', encoding='utf-8') as archivo:
        return [{'planta': fila['planta'], 'consumo_kwh': float(fila['consumo_kwh'])} for fila in csv.DictReader(archivo)]

def vista_panel_sustentabilidad(request):
    registros = cargar_registros_csv(RUTA_CSV)
    metricas = obtener_metricas_consumo(registros)
    contexto = {'titulo': 'Panel de Sustentabilidad', 'total_emisiones': metricas['total_emisiones'], 'planta_mayor_consumo': metricas['planta_mayor_consumo'], 'emisiones_por_planta': metricas['emisiones_por_planta']}
    return render(request, 'sustentabilidad/panel.html', contexto)
