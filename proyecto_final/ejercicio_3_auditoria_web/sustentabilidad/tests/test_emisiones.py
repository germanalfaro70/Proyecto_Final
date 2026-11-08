import unittest
from sustentabilidad.emisiones import calcular_emisiones_carbono

class TestCalculoEmisiones(unittest.TestCase):

    def test_valor_nominal_con_factor_por_defecto(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(100), 40.0)

    def test_factor_personalizado(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(250, 0.5), 125.0)

    def test_consumo_cero_da_cero_emisiones(self):
        self.assertEqual(calcular_emisiones_carbono(0), 0)

    def test_consumo_decimal(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(12.5), 5.0)

    def test_consumo_negativo_lanza_value_error(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-1)

    def test_factor_cero_con_consumo_positivo(self):
        self.assertEqual(calcular_emisiones_carbono(500, 0), 0)
if __name__ == '__main__':
    unittest.main()
