from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
from .models import Pelicula, Transaccion

class PeliculaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.pelicula = Pelicula.objects.create(
            titulo='Titulo 1', 
            director='Director 1', 
            genero='genero 1',
            precio_compra=100.00,
            precio_arriendo=50.00,
            stock=4
        )

    def test_nombre(self):
        pelicula = Pelicula.objects.get(id=self.pelicula.id)
        self.assertEqual(pelicula.titulo, 'Titulo 1')

    def test_director(self):
        pelicula = Pelicula.objects.get(id=self.pelicula.id)
        self.assertEqual(pelicula.director, 'Director 1')


    def test_genero(self):
        pelicula = Pelicula.objects.get(id=self.pelicula.id)
        self.assertEqual(pelicula.genero, 'genero 1')
        
    def test_precio_compra(self):
        pelicula = Pelicula.objects.get(id=self.pelicula.id)
        self.assertEqual(pelicula.precio_compra, 100.00)

    def test_precio_arriendo(self):
        pelicula = Pelicula.objects.get(id=self.pelicula.id)
        self.assertEqual(pelicula.precio_arriendo, 50.00)

    def test_stock(self):
        pelicula = Pelicula.objects.get(id=self.pelicula.id)
        self.assertEqual(pelicula.stock, 4)

        
class PeliculaUrlTest(TestCase):

    def test_pelicula_url(self):
        response = self.client.get(reverse('lista_usuarios'))  
        self.assertEqual(response.status_code, 200)

class TransaccionViewTest(TestCase):
    def test_transacciones_view(self):
        url = reverse('lista_transacciones') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventario/transacciones.html')         
        self.assertContains(response, 'Nombre')          
        self.assertContains(response, 'Ciudad')
        self.assertContains(response, 'País')
        self.assertContains(response, 'Fecha_inicio')          
        self.assertContains(response, 'Fecha_termino')
        self.assertContains(response, 'Estado')
        self.assertNotContains(response, 'NO ES LA RESPUESTA ESPERADA')
        print('Esto es todo , muchas gracias')
        print('LMM')

