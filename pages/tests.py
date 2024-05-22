from django.test import TestCase
from django.urls import reverse
from .models import Ropa
from .forms import RopaForm

class RopaCreateViewTests(TestCase):

    def setUp(self):
        # Datos de prueba válidos
        self.valid_data = {
            'Titulo': 'Camisa',
            'Marca': 'MarcaX',
            'Fecha_publicacion': '2024-05-20T00:00:00Z',
            'precio': 100,
            'image_url': 'https://example.com/image.jpg'
        }
        # Datos de prueba inválidos
        self.invalid_data = {
            'Titulo': '',
            'Marca': 'MarcaY',
            'Fecha_publicacion': '2024-05-20T00:00:00Z',
            'precio': -50,
            'image_url': 'https://example.com/image.jpg'
        }

    def test_create_ropa_valid_data(self):
        response = self.client.post(reverse('ropa_create'), self.valid_data)
        self.assertEqual(response.status_code, 302)  # Debe redirigir al 'ropa_index'
        self.assertEqual(Ropa.objects.count(), 1)  # Debe haberse creado una instancia
        ropa = Ropa.objects.first()
        self.assertEqual(ropa.Titulo, 'Camisa')
        self.assertEqual(ropa.Marca, 'MarcaX')
        self.assertEqual(ropa.precio, 100)
        self.assertEqual(ropa.image_url, 'https://example.com/image.jpg')

    def test_create_ropa_invalid_data(self):
        response = self.client.post(reverse('ropa_create'), self.invalid_data)
        
        
        self.assertEqual(response.status_code, 200)  # Debe mostrar el formulario con errores
        self.assertEqual(Ropa.objects.count(), 0)  # No debe haberse creado ninguna instancia
        self.assertContains(response, "Este campo es obligatorio")  # Chequea los errores del formulario
        self.assertContains(response, "Asegúrate de que este valor sea mayor o igual a 0")

    def test_get_create_ropa_view(self):
        response = self.client.get(reverse('ropa_create'))
        
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ropa/create.html')
        self.assertContains(response, 'Crear Ropa')
        self.assertIsInstance(response.context['form'], RopaForm)