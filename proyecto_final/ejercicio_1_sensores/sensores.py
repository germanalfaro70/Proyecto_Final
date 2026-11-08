import re
UBICACION_POR_DEFECTO = 'Sin ubicación'
PATRON_NUMERO = re.compile('-?\\d+(?:\\.\\d+)?')

def limpiar_registro_sensor(registro_raw):
    sensor_id = str(registro_raw.get('sensor_id', '')).strip()
    texto_temp = str(registro_raw.get('temperatura', '')).replace(',', '.')
    coincidencia = PATRON_NUMERO.search(texto_temp)
    temperatura = float(coincidencia.group()) if coincidencia else None
    ubicacion = str(registro_raw.get('ubicacion') or '').strip()
    if not ubicacion:
        ubicacion = UBICACION_POR_DEFECTO
    return {'sensor_id': sensor_id, 'temperatura': temperatura, 'ubicacion': ubicacion}

def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    alertas = []
    temperaturas = []
    for sensor in lista_sensores_limpios:
        temp = sensor['temperatura']
        if temp is None:
            continue
        temperaturas.append(temp)
        if temp > umbral_temperatura:
            alertas.append(sensor['sensor_id'])
    promedio = sum(temperaturas) / len(temperaturas) if temperaturas else 0.0
    return (alertas, promedio)
if __name__ == '__main__':
    registros_crudos = [{'sensor_id': ' SENSOR-001 ', 'temperatura': '24.5C', 'ubicacion': 'Planta Norte'}, {'sensor_id': 'SENSOR-002', 'temperatura': '31,0 °C', 'ubicacion': ''}, {'sensor_id': 'SENSOR-003 ', 'temperatura': '27C', 'ubicacion': 'Planta Sur'}, {'sensor_id': 'SENSOR-004', 'temperatura': '', 'ubicacion': 'Depósito'}, {'sensor_id': 'SENSOR-005', 'temperatura': '33.8C', 'ubicacion': 'Planta Este'}]
    limpios = [limpiar_registro_sensor(r) for r in registros_crudos]
    alertas, promedio = generar_resumen_sensores(limpios, umbral_temperatura=30.0)
    print('=' * 40)
    print('REPORTE DE SENSORES')
    print('=' * 40)
    print(f'Sensores en alerta: {(', '.join(alertas) if alertas else 'Ninguno')}')
    print(f'Temperatura promedio: {promedio:.2f} °C')
    print('=' * 40)
