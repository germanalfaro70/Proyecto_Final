import unittest
from sustentabilidad.metricas import obtener_metricas_consumo

class TestObtenerMetricas(unittest.TestCase):

    def test_total_y_planta_mayor(self):
        registros = [{'planta': 'Norte', 'consumo_kwh': 1000}, {'planta': 'Sur', 'consumo_kwh': 500}, {'planta': 'Norte', 'consumo_kwh': 200}]
        metricas = obtener_metricas_consumo(registros)
        self.assertEqual(metricas['total_emisiones'], 680.0)
        self.assertEqual(metricas['planta_mayor_consumo'], 'Norte')
        self.assertEqual(metricas['emisiones_por_planta'], {'Norte': 480.0, 'Sur': 200.0})

    def test_lista_vacia(self):
        metricas = obtener_metricas_consumo([])
        self.assertEqual(metricas['total_emisiones'], 0)
        self.assertIsNone(metricas['planta_mayor_consumo'])

    def test_consumo_negativo_propaga_value_error(self):
        with self.assertRaises(ValueError):
            obtener_metricas_consumo([{'planta': 'Norte', 'consumo_kwh': -10}])
if __name__ == '__main__':
    unittest.main()
