"""
Cálculo de promedio general y por categoría (por ejemplo: promedio de ventas, notas, reservas, etc.).
- Porcentajes relativos de categorías sobre el total general (por ejemplo: porcentaje
de usuarios activos, productos más vendidos, reservas realizadas, etc.).
- Resumen estadístico simple: total, promedio, valor máximo, valor mínimo y conteos
específicos.

- Otras estadísticas que el grupo considere pertinentes en función de la temática elegida.
Importante: Las funcionalidades estadísticas podrán ampliarse en la segunda entrega.

Terminado:
- Identificación de valores máximos y mínimos en los registros (por ejemplo: la mayor
o menor venta, el estudiante con mejor o peor promedio, etc.).
- Conteo de registros totales y discriminados según categorías específicas.
- Conteo de registros totales y discriminados según categorías específicas.

"""

from constantes import *

def obtener_menor_venta(ventas):
    min = ventas[0]
    for v in ventas:
        if v[TOTAL_VENTA] < min[TOTAL_VENTA]:
            min = v

    return min

def obtener_mayor_venta(ventas):
    max = ventas[0]
    for v in ventas:
        if v[TOTAL_VENTA] > max[TOTAL_VENTA]:
            max = v

    return max

def obtener_ventas_por_vendedor(ventas, vendedor):
    cont = 0
    for v in ventas:
        if vendedor == v[VENDEDOR]:
            cont +=1

    return cont

def obtener_ventas_por_cada_vendedor(ventas):
    vendedores = []

    for v in ventas:
        if v[VENDEDOR] not in vendedores:
            vendedores.append(v[VENDEDOR])

    for vendedor in vendedores:
        print("Ventas de", vendedor)

        for v in ventas:
            if v[VENDEDOR] == vendedor:
                print(v)

def obtener_cant_total_ventas(ventas):
    return len(ventas)
