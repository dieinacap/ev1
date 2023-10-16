from decimal import Decimal
from django.db import models

class Importacion(models.Model):
    cantidad_unidades = models.PositiveIntegerField()
    costo_unitario_usd = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_articulo = models.CharField(max_length=100)
    codigo_articulo = models.CharField(max_length=50)
    nombre_proveedor = models.CharField(max_length=100)
    costo_envio_usd = models.DecimalField(max_digits=10, decimal_places=2)

    def calcular_total_pedido(self):
        return self.cantidad_unidades * self.costo_unitario_usd

    def calcular_total_impuestos(self):
        valor_cif = self.costo_envio_usd + self.calcular_total_pedido()
        tasa_aduana = valor_cif * Decimal('0.06')
        iva = valor_cif * Decimal('0.19')
        return tasa_aduana, iva