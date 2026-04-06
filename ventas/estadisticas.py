from .constantes import *

AZUL     = "\033[34m"
RESET = "\033[0m"

ancho_standard = 100

def mostrar_linea_divisoria(ancho_total):
    print(f"{AZUL}{'-'*ancho_total}{RESET}")

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

def obtener_ventas_por_cada_vendedor(ventas):
    ventas_activas = list(filter(lambda x: x[ACTIVO] is True, ventas))
    vendedores = []

    mostrar_linea_divisoria(ancho_standard)
    for v in ventas_activas:
        if v[VENDEDOR] not in vendedores:
            vendedores.append(v[VENDEDOR])

    for vendedor in vendedores:
        print("Ventas de", vendedor)
        for v in ventas_activas:
            if v[VENDEDOR] == vendedor:
                print(v)

    mostrar_linea_divisoria(ancho_standard)


def obtener_articulo_mas_vendido(ventas):
    cantidades = {}

    mostrar_linea_divisoria(ancho_standard)
    for venta in ventas:
        for articulo in venta[ARTICULOS]:
            cantidades[articulo[0]] = cantidades.get(articulo[0], 0) + articulo[1]

    if not cantidades:
        print("No hay artículos vendidos.")
        return
    
    articulo = max(cantidades, key=cantidades.get)
    print("Cantidades:", cantidades)
    print("Artículo más vendido:", articulo)
    print("Cantidad total de unidades vendidas:", cantidades[articulo])
    mostrar_linea_divisoria(ancho_standard)



def obtener_cant_total_ventas(ventas):
    ventas_activas = list(filter(lambda x: x[ACTIVO] is True, ventas))
    mostrar_linea_divisoria(ancho_standard)
    print("La cantidad de ventas total es: ", len(ventas_activas))
    mostrar_linea_divisoria(ancho_standard)

    return
