from .constantes import *
from productos.productos import mostrar_productos

# Programa principal
RESET = "\033[0m"
BOLD  = "\033[1m"
# Colores
ROJO     = "\033[31m"
VERDE    = "\033[32m"
AMARILLO = "\033[33m"
AZUL     = "\033[34m"
CYAN     = "\033[36m"
BLANCO   = "\033[37m"
# Combinados
BOLD_AZUL   = "\033[1;34m"
BOLD_CYAN   = "\033[1;36m"
BOLD_VERDE  = "\033[1;32m"
BOLD_ROJO   = "\033[1;31m"
BOLD_AMARILLO = "\033[1;33m"

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
    print(f"{BOLD}Ventas por vendedor{RESET}")

    for v in ventas_activas:
        if v[VENDEDOR] not in vendedores:
            vendedores.append(v[VENDEDOR])

    encabezados = ["ID", "Fecha", "Total", "Cliente", "Productos"]

    for vendedor in vendedores:
        mostrar_linea_divisoria(ancho_standard)
        print(f"{BOLD}Vendedor: {AMARILLO}{vendedor}{RESET}")
        print()
        print(
            f"{BOLD}"
            f"{encabezados[0]:<8} | "
            f"{encabezados[1]:<13} | "
            f"{encabezados[2]:<13} | "
            f"{encabezados[3]:<26} | "
            f"{encabezados[4]:<20}"
            f"{RESET}"
        )
        mostrar_linea_divisoria(ancho_standard)

        for v in ventas_activas:
            if v[VENDEDOR] == vendedor:
                productos_str = ', '.join([f"id:{p[0]} x{p[1]}" for p in v[ARTICULOS]])
                print(
                    f"{AMARILLO}{str(v[ID]):<8}{RESET} | "
                    f"{str(v[FECHA]):<13} | "
                    f"{('$' + format(float(v[TOTAL_VENTA]), '.2f')):<13} | "
                    f"{str(v[CLIENTE]):<26} | "
                    f"{CYAN}{productos_str:<20}{RESET}"
                )

    mostrar_linea_divisoria(ancho_standard)


def obtener_articulo_mas_vendido(ventas):
    cantidades = {}

    mostrar_linea_divisoria(ancho_standard)
    print(f"{BOLD}Artículo más vendido{RESET}")
    mostrar_linea_divisoria(ancho_standard)

    for venta in ventas:
        for articulo in venta[ARTICULOS]:
            cantidades[articulo[0]] = cantidades.get(articulo[0], 0) + articulo[1]

    if not cantidades:
        print("No hay artículos vendidos.")
        return
    
    articulo = max(cantidades, key=cantidades.get)
    mostrar_productos([[articulo, cantidades[articulo]]])
    mostrar_linea_divisoria(ancho_standard)



def obtener_cant_total_ventas(ventas):
    ventas_activas = list(filter(lambda x: x[ACTIVO] is True, ventas))
    mostrar_linea_divisoria(ancho_standard)
    print("La cantidad de ventas total es: ", len(ventas_activas))
    mostrar_linea_divisoria(ancho_standard)

    return
