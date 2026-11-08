FACTOR_EMISION_POR_DEFECTO = 0.4

def calcular_emisiones_carbono(consumo_kwh, factor_emision=FACTOR_EMISION_POR_DEFECTO):
    if consumo_kwh < 0:
        raise ValueError('El consumo no puede ser negativo')
    return consumo_kwh * factor_emision
