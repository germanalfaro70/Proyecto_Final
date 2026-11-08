import json
import os
import tempfile
import unittest
from productos import DispositivoEcologico, GestorInventario, PanelSolar, StockInvalidoError

class TestStock(unittest.TestCase):

    def test_stock_negativo_en_constructor_lanza_error(self):
        with self.assertRaises(StockInvalidoError):
            DispositivoEcologico('Turbina', 10, -1)

    def test_setter_rechaza_negativo_y_conserva_valor_anterior(self):
        dispositivo = DispositivoEcologico('Turbina', 10, 5)
        with self.assertRaises(StockInvalidoError):
            dispositivo.stock = -2
        self.assertEqual(dispositivo.stock, 5)

class TestPanelSolar(unittest.TestCase):

    def test_es_subclase_de_dispositivo(self):
        self.assertIsInstance(PanelSolar('Pro', 100, 2, 450, 21.5), DispositivoEcologico)

    def test_ficha_tecnica_propia(self):
        ficha = PanelSolar('Pro', 100, 2, 450, 21.5).ficha_tecnica()
        self.assertIn('[PANEL SOLAR]', ficha)
        self.assertIn('450 W', ficha)

class TestGestorInventario(unittest.TestCase):

    def test_guarda_json_con_tipo_y_atributos(self):
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = os.path.join(carpeta, 'catalogo.json')
            GestorInventario().guardar_catalogo_json([PanelSolar('Pro', 100, 2, 450, 21.5)], ruta)
            with open(ruta, encoding='utf-8') as archivo:
                datos = json.load(archivo)
        self.assertEqual(datos[0]['tipo'], 'PanelSolar')
        self.assertEqual(datos[0]['potencia_w'], 450)
if __name__ == '__main__':
    unittest.main()
