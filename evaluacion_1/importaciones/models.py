from decimal import Decimal
from django.db import models


VALOR_DOLAR = 890

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
        
        # Calcula la tasa de aduana en dólares
        tasa_aduana_usd = valor_cif * Decimal('0.06')
        
        # Convierte la tasa de aduana a pesos chilenos usando el tipo de cambio (VALOR_DOLAR)
        tasa_aduana_clp = tasa_aduana_usd * VALOR_DOLAR
        
        # Calcula el IVA en dólares
        iva_usd = valor_cif * Decimal('0.19')
        
        # Convierte el IVA a pesos chilenos usando el tipo de cambio (VALOR_DOLAR)
        iva_clp = iva_usd * VALOR_DOLAR
        
        return tasa_aduana_clp, iva_clp