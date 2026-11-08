import unittest
from sensores import UBICACION_POR_DEFECTO, generar_resumen_sensores, limpiar_registro_sensor

class TestLimpiarRegistro(unittest.TestCase):

    def test_limpia_id_y_temperatura(self):
        resultado = limpiar_registro_sensor({'sensor_id': ' SENSOR-001 ', 'temperatura': '24.5C', 'ubicacion': 'Planta Norte'})
        self.assertEqual(resultado, {'sensor_id': 'SENSOR-001', 'temperatura': 24.5, 'ubicacion': 'Planta Norte'})

    def test_ubicacion_vacia_usa_valor_por_defecto(self):
        resultado = limpiar_registro_sensor({'sensor_id': 'S-2', 'temperatura': '20C', 'ubicacion': '  '})
        self.assertEqual(resultado['ubicacion'], UBICACION_POR_DEFECTO)

    def test_ubicacion_ausente_usa_valor_por_defecto(self):
        resultado = limpiar_registro_sensor({'sensor_id': 'S-3', 'temperatura': '20C'})
        self.assertEqual(resultado['ubicacion'], UBICACION_POR_DEFECTO)

    def test_acepta_coma_decimal(self):
        resultado = limpiar_registro_sensor({'sensor_id': 'S-4', 'temperatura': '31,0 °C'})
        self.assertEqual(resultado['temperatura'], 31.0)

    def test_temperatura_vacia_es_none(self):
        resultado = limpiar_registro_sensor({'sensor_id': 'S-5', 'temperatura': ''})
        self.assertIsNone(resultado['temperatura'])

class TestResumenSensores(unittest.TestCase):

    def test_detecta_alertas_y_calcula_promedio(self):
        sensores = [{'sensor_id': 'A', 'temperatura': 20.0, 'ubicacion': 'x'}, {'sensor_id': 'B', 'temperatura': 32.0, 'ubicacion': 'x'}, {'sensor_id': 'C', 'temperatura': 30.0, 'ubicacion': 'x'}]
        alertas, promedio = generar_resumen_sensores(sensores, 30.0)
        self.assertEqual(alertas, ['B'])
        self.assertAlmostEqual(promedio, 82 / 3)

    def test_ignora_sensores_sin_temperatura(self):
        sensores = [{'sensor_id': 'A', 'temperatura': 25.0, 'ubicacion': 'x'}, {'sensor_id': 'B', 'temperatura': None, 'ubicacion': 'x'}]
        _, promedio = generar_resumen_sensores(sensores, 30.0)
        self.assertEqual(promedio, 25.0)

    def test_lista_vacia(self):
        self.assertEqual(generar_resumen_sensores([], 30.0), ([], 0.0))
if __name__ == '__main__':
    unittest.main()
