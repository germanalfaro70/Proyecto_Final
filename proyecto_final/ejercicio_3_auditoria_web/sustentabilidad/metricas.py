from .emisiones import calcular_emisiones_carbono

def obtener_metricas_consumo(registros):
    consumo_por_planta = {}
    for registro in registros:
        planta = registro['planta']
        consumo_por_planta[planta] = consumo_por_planta.get(planta, 0) + registro['consumo_kwh']
    emisiones_por_planta = {planta: round(calcular_emisiones_carbono(consumo), 2) for planta, consumo in consumo_por_planta.items()}
    total_emisiones = round(sum(emisiones_por_planta.values()), 2)
    planta_mayor_consumo = max(consumo_por_planta, key=consumo_por_planta.get) if consumo_por_planta else None
    return {'total_emisiones': total_emisiones, 'planta_mayor_consumo': planta_mayor_consumo, 'emisiones_por_planta': emisiones_por_planta}
