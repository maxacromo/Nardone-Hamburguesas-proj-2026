from .constantes import *
from productos.productos import mostrar_productos_seleccionados

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

    ventas_activas = list(filter(lambda x: x[ACTIVO] is True, ventas))

    for venta in ventas_activas:
        for articulo in venta[ARTICULOS]:
            codigo = int(articulo[0])
            cantidades[codigo] = cantidades.get(codigo, 0) + articulo[1]

    if not cantidades:
        print("No hay artículos vendidos.")
        return

    articulo = max(cantidades, key=cantidades.get)
    mostrar_productos_seleccionados([[articulo, cantidades[articulo]]])
    mostrar_linea_divisoria(ancho_standard)



def obtener_articulo_menos_vendido(ventas):
    cantidades = {}

    mostrar_linea_divisoria(ancho_standard)
    print(f"{BOLD}Artículo menos vendido{RESET}")
    mostrar_linea_divisoria(ancho_standard)

    ventas_activas = list(filter(lambda x: x[ACTIVO] is True, ventas))

    for venta in ventas_activas:
        for articulo in venta[ARTICULOS]:
            codigo = int(articulo[0])
            cantidades[codigo] = cantidades.get(codigo, 0) + articulo[1]

    if not cantidades:
        print("No hay artículos vendidos.")
        return

    articulo = min(cantidades, key=cantidades.get)
    mostrar_productos_seleccionados([[articulo, cantidades[articulo]]])
    mostrar_linea_divisoria(ancho_standard)


def obtener_cant_total_ventas(ventas):
    ventas_activas = list(filter(lambda x: x[ACTIVO] is True, ventas))
    total_recaudado = sum(v[TOTAL_VENTA] for v in ventas_activas)
    mostrar_linea_divisoria(ancho_standard)
    promedio = total_recaudado / len(ventas_activas) if ventas_activas else 0
    print(f"Cantidad de ventas total: {AMARILLO}{len(ventas_activas)}{RESET}")
    print(f"Total recaudado:          {AMARILLO}${total_recaudado:.2f}{RESET}")
    print(f"Promedio por venta:       {AMARILLO}${promedio:.2f}{RESET}")
    mostrar_linea_divisoria(ancho_standard)


def obtener_porcentajes_relativos(ventas):
    from productos.productos import crear_productos
    ventas_activas = list(filter(lambda x: x[ACTIVO] is True, ventas))
    total_general = sum(v[TOTAL_VENTA] for v in ventas_activas)

    mostrar_linea_divisoria(ancho_standard)
    print(f"{BOLD}Porcentajes relativos sobre el total de ventas{RESET}")
    mostrar_linea_divisoria(ancho_standard)
    print("[1] Por vendedor")
    print("[2] Por producto")
    mostrar_linea_divisoria(ancho_standard)
    opcion = input("Seleccione una opcion: ").strip()

    if opcion == "1":
        totales_vendedor = {}
        for v in ventas_activas:
            totales_vendedor[v[VENDEDOR]] = totales_vendedor.get(v[VENDEDOR], 0) + v[TOTAL_VENTA]

        mostrar_linea_divisoria(ancho_standard)
        print(f"{BOLD}Participacion por vendedor{RESET}")
        mostrar_linea_divisoria(ancho_standard)
        print(f"{BOLD}{'Vendedor':<26} | {'Total vendido':<15} | {'Porcentaje'}{RESET}")
        mostrar_linea_divisoria(ancho_standard)
        for vendedor, total in sorted(totales_vendedor.items(), key=lambda x: x[1], reverse=True):
            porcentaje = (total / total_general * 100) if total_general else 0
            print(
                f"{vendedor:<26} | "
                f"${total:<14.2f} | "
                f"{BOLD_VERDE}{porcentaje:.1f}%{RESET}"
            )

    elif opcion == "2":
        productos = crear_productos()
        cantidades_producto = {}
        for v in ventas_activas:
            for art in v[ARTICULOS]:
                codigo = int(art[0])
                cantidades_producto[codigo] = cantidades_producto.get(codigo, 0) + art[1]

        total_articulos = sum(cantidades_producto.values())

        mostrar_linea_divisoria(ancho_standard)
        print(f"{BOLD}Participacion por producto{RESET}")
        mostrar_linea_divisoria(ancho_standard)
        print(f"{BOLD}{'Producto':<26} | {'Unidades vendidas':<18} | {'Porcentaje'}{RESET}")
        mostrar_linea_divisoria(ancho_standard)
        for codigo, cant in sorted(cantidades_producto.items(), key=lambda x: x[1], reverse=True):
            nombre = next((p[1] for p in productos if p[0] == codigo), str(codigo))
            porcentaje = (cant / total_articulos * 100) if total_articulos else 0
            print(
                f"{nombre:<26} | "
                f"{cant:<18} | "
                f"{BOLD_VERDE}{porcentaje:.1f}%{RESET}"
            )
    else:
        print("Opcion invalida.")

    mostrar_linea_divisoria(ancho_standard)


def obtener_promedio_por_dia(ventas):
    ventas_activas = list(filter(lambda x: x[ACTIVO] is True, ventas))

    totales_por_dia = {}
    for v in ventas_activas:
        fecha = v[FECHA]
        totales_por_dia[fecha] = totales_por_dia.get(fecha, 0) + v[TOTAL_VENTA]

    mostrar_linea_divisoria(ancho_standard)
    print(f"{BOLD}Promedio de ventas por día{RESET}")
    mostrar_linea_divisoria(ancho_standard)

    if not totales_por_dia:
        print("No hay ventas registradas.")
        mostrar_linea_divisoria(ancho_standard)
        return

    print(f"{BOLD}{'Fecha':<14} | {'Total del día':<15} | {'Cant. ventas':<13} | {'Promedio'}{RESET}")
    mostrar_linea_divisoria(ancho_standard)

    for fecha in sorted(totales_por_dia):
        cant = sum(1 for v in ventas_activas if v[FECHA] == fecha)
        promedio_dia = totales_por_dia[fecha] / cant
        print(
            f"{AMARILLO}{fecha:<14}{RESET} | "
            f"${totales_por_dia[fecha]:<14.2f} | "
            f"{cant:<13} | "
            f"{BOLD_VERDE}${promedio_dia:.2f}{RESET}"
        )

    promedio_global = sum(totales_por_dia.values()) / len(totales_por_dia)
    mostrar_linea_divisoria(ancho_standard)
    print(f"Promedio diario general: {BOLD_VERDE}${promedio_global:.2f}{RESET}")
    mostrar_linea_divisoria(ancho_standard)


def reporte_completo(ventas):
    from productos.productos import crear_productos
    productos = crear_productos()
    ventas_activas = list(filter(lambda x: x[ACTIVO] is True, ventas))
    total_general = sum(v[TOTAL_VENTA] for v in ventas_activas)
    promedio = total_general / len(ventas_activas) if ventas_activas else 0

    mostrar_linea_divisoria(ancho_standard)
    print(f"{BOLD}REPORTE ESTADÍSTICO COMPLETO{RESET}")

    # Totales generales
    mostrar_linea_divisoria(ancho_standard)
    print(f"{BOLD}RESUMEN GENERAL{RESET}")
    mostrar_linea_divisoria(ancho_standard)
    print(f"  Cantidad de ventas : {AMARILLO}{len(ventas_activas)}{RESET}")
    print(f"  Total recaudado    : {AMARILLO}${total_general:.2f}{RESET}")
    print(f"  Promedio por venta : {AMARILLO}${promedio:.2f}{RESET}")

    # Articulo mas y menos vendido
    cantidades = {}
    for v in ventas_activas:
        for art in v[ARTICULOS]:
            codigo = int(art[0])
            cantidades[codigo] = cantidades.get(codigo, 0) + art[1]

    if cantidades:
        cod_max = max(cantidades, key=cantidades.get)
        cod_min = min(cantidades, key=cantidades.get)
        nombre_max = next((p[1] for p in productos if p[0] == cod_max), str(cod_max))
        nombre_min = next((p[1] for p in productos if p[0] == cod_min), str(cod_min))
        mostrar_linea_divisoria(ancho_standard)
        print(f"{BOLD}PRODUCTOS{RESET}")
        mostrar_linea_divisoria(ancho_standard)
        print(f"  Más vendido  : {AMARILLO}{nombre_max}{RESET} ({cantidades[cod_max]} unidades)")
        print(f"  Menos vendido: {AMARILLO}{nombre_min}{RESET} ({cantidades[cod_min]} unidades)")

    # Top vendedores
    totales_vendedor = {}
    for v in ventas_activas:
        totales_vendedor[v[VENDEDOR]] = totales_vendedor.get(v[VENDEDOR], 0) + v[TOTAL_VENTA]

    mostrar_linea_divisoria(ancho_standard)
    print(f"{BOLD}VENDEDORES{RESET}")
    mostrar_linea_divisoria(ancho_standard)
    for vendedor, total in sorted(totales_vendedor.items(), key=lambda x: x[1], reverse=True):
        porcentaje = (total / total_general * 100) if total_general else 0
        print(f"  {vendedor:<26} ${total:<12.2f} {BOLD_VERDE}{porcentaje:.1f}%{RESET}")

    mostrar_linea_divisoria(ancho_standard)
