from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    genero = models.CharField(
        choices=[('Ciencia Ficción', 'ciencia ficción'), ('Terror', 'terror'), ('Suspenso', 'suspenso'), 
                ('Romantica', 'romantica'), ('Comedia', 'comedia'), ('Acción', 'acción'), ('Drama', 'drama'), ('Crimen', 'crimen'), ('Animación', 'animación')],
        max_length=100
    )
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_arriendo = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    
    def __str__(self):
        return self.titulo
    
class Transaccion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    tipo = models.CharField(
        choices=[('Arriendo', 'arriendo'), ('Compra', 'compra')],
        max_length=100
    )
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_termino = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(
        choices=[('Completado', 'completado'), ('Pendiente', 'pendiente')],
        max_length=50
    )
    class Meta:
        verbose_name = "Inventario"
        verbose_name_plural = "Inventarios"
        permissions = (
                ("development", "Puede desarrollar"),
                ("scrum_master", "Es Scrum Master"),
                ("visualizar_listado", "visualizar listado"),
                ("superuser", "superuser" )
        )
    
    def __str__(self):
        return f"{self.usuario} - {self.pelicula}"
    
    