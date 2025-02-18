from django.db import models

# Create your models here.
from django.db import models

class Producto(models.Model):
    descripcion = models.CharField(max_length=100, unique=True)  # Nombre del producto (único)
    unidad = models.CharField(max_length=20)  # Unidad (ej., KG, Manojo, Piezas)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)  # Precio por unidad
    impuesto = models.DecimalField(max_digits=2, decimal_places=0)
    codigoo = models.DecimalField(max_digits=10, decimal_places=0)
    detalles = models.TextField(blank=True)  # Descripción adicional del producto (opcional)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name="producto"
        verbose_name_plural="productos"
    
#Descripcion igual al nombre
#Validacion(Descripcion del Producto) -------Producto(Abarrote,Carnico-Lacteo,Verduras)