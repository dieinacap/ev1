from django.shortcuts import render, redirect
from .models import Importacion

VALOR_DOLAR = 890

def importacion(request):
    
    if request.method == 'POST':
        cantidad_unidades = int(request.POST['cantidad_unidades'])
        costo_unitario_usd = float(request.POST['costo_unitario_usd'])
        nombre_articulo = request.POST['nombre_articulo']
        codigo_articulo = request.POST['codigo_articulo']
        nombre_proveedor = request.POST['nombre_proveedor']
        costo_envio_usd = float(request.POST['costo_envio_usd'])

        if cantidad_unidades <= 0 or not costo_unitario_usd or not nombre_articulo or not codigo_articulo or not nombre_proveedor or costo_envio_usd < 0:
            pass
        else:
            simulacion = Importacion(
                cantidad_unidades=cantidad_unidades,
                costo_unitario_usd=costo_unitario_usd,
                nombre_articulo=nombre_articulo,
                codigo_articulo=codigo_articulo,
                nombre_proveedor=nombre_proveedor,
                costo_envio_usd=costo_envio_usd
            )
            simulacion.save()
            return redirect('lista_simulaciones')

    return render(request, 'importacion.html')

from decimal import Decimal  # Importa Decimal

def lista_simulaciones(request):
    simulaciones = Importacion.objects.all()
    
    for simulacion in simulaciones:
        simulacion.total_pedido = simulacion.calcular_total_pedido()
        impuestos = simulacion.calcular_total_impuestos()
        simulacion.tasa_aduana = Decimal(impuestos[0])
        simulacion.iva = Decimal(impuestos[1]) 
        simulacion.total_en_clp = (
            simulacion.total_pedido + Decimal(simulacion.costo_envio_usd) * VALOR_DOLAR  + simulacion.tasa_aduana + simulacion.iva
        )
    
    return render(request, 'lista_simulaciones.html', {'simulaciones': simulaciones})
