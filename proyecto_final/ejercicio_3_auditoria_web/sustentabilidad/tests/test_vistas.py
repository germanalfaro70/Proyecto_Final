from django.test import RequestFactory, SimpleTestCase
from sustentabilidad.views import vista_panel_sustentabilidad

class TestVistaPanelSustentabilidad(SimpleTestCase):

    def test_responde_200_y_renderiza_plantilla(self):
        request = RequestFactory().get('/sustentabilidad/panel/')
        response = vista_panel_sustentabilidad(request)
        contenido = response.content.decode('utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Panel de Sustentabilidad', contenido)
        self.assertIn('Planta Este', contenido)

    def test_url_del_panel_resuelve_a_la_vista(self):
        from django.urls import resolve, reverse
        url = reverse('sustentabilidad:panel')
        self.assertEqual(resolve(url).func, vista_panel_sustentabilidad)
