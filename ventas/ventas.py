from .constantes import *

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

encabezados = ['Id', 'Empleado', 'Cliente', 'Total', 'Fecha' ,'Articulos y Cantidad']
elementos = [
    ['1', 'Ezequiel Gonzalez', 'Juan Perez', 100, '31-01-2026', [['A001', 1], ['A002', 2]], True],
    ['2', 'Ezequiel Gonzalez', 'Pepe Alvarez', 130, '02-02-2026', [['A003', 1], ['A004', 1]], True],
    ['3', 'Ezequiel Gonzalez', 'Pedro Lopez', 105, '06-02-2026', [['A001', 1], ['A005', 1]], True],
    ['4', 'Juan Perez', 'Pedro Lopez', 1052, '01-03-2026', [['A006', 2], ['A007', 3]], True],
    ['5', 'Juan Perez', 'Pedro Lopez', 2050, '01-03-2026', [['A008', 1], ['A009', 5]], True],
    ['6', 'Juan Perez', 'Pedro Lopez', 500, '01-03-2026', [['A002', 4], ['A010', 1]], True],
    ['7', 'Maria Lopez', 'Carlos Diaz', 890, '05-03-2026', [['A003', 2], ['A004', 3]], True],
    ['8', 'Maria Lopez', 'Ana Torres', 450, '05-03-2026', [['A005', 1], ['A001', 2]], True],
    ['9', 'Lucas Fernandez', 'Juan Perez', 1200, '10-03-2026', [['A011', 2], ['A012', 1]], True],
    ['10', 'Lucas Fernandez', 'Sofia Gomez', 750, '10-03-2026', [['A007', 1], ['A003', 2]], True],
    ['11', 'Kenaya Zalles', 'Lucia Martinez', 320, '12-03-2026', [['A002', 2], ['A006', 1]], True],
    ['12', 'Juan Perez', 'Diego Suarez', 980, '15-03-2026', [['A009', 2], ['A001', 3]], True],
    ['13', 'Maria Lopez', 'Valentina Ruiz', 1500, '16-03-2026', [['A010', 1], ['A011', 2]], True],
    ['14', 'Lucas Fernandez', 'Martin Acosta', 670, '18-03-2026', [['A004', 2], ['A008', 1]], True],
    ['15', 'Ezequiel Gonzalez', 'Camila Benitez', 430, '20-03-2026', [['A003', 1], ['A005', 2]], True],
    ['16', 'Juan Perez', 'Fernando Silva', 2500, '22-03-2026', [['A012', 4], ['A006', 2]], True],
    ['17', 'Maria Lopez', 'Pedro Lopez', 300, '22-03-2026', [['A001', 1], ['A007', 1]], True],
    ['18', 'Lucas Fernandez', 'Juan Perez', 1100, '25-03-2026', [['A009', 2], ['A010', 2]], True],
    ['19', 'Ezequiel Gonzalez', 'Pepe Alvarez', 870, '27-03-2026', [['A002', 3], ['A011', 1]], True],
    ['20', 'Juan Perez', 'Carlos Diaz', 1990, '28-03-2026', [['A008', 2], ['A012', 3], ['A005', 5]], True]
]

def mostrar_linea_divisoria(ancho_total):
    print(f"{AZUL}{'-'*ancho_total}{RESET}")
    
def formatear_articulos(articulos):
    return ", ".join([f"{cod}({cant})" for cod, cant in articulos])

def mostrar_venta(venta):
    print(f"ID: {AMARILLO}{venta[ID]}{RESET}")
    print(f"Empleado: {AMARILLO}{venta[VENDEDOR]}{RESET}")
    print(f"Cliente: {AMARILLO}{venta[CLIENTE]}{RESET}")
    print(f"Total: {AMARILLO}${venta[TOTAL_VENTA]}{RESET}")
    print(f"Fecha: {AMARILLO}{venta[FECHA]}{RESET}")
    print(f"Articulos: {AMARILLO}{formatear_articulos(venta[ARTICULOS])}{RESET}")


# Para calcular el Id, obtengo el Id del ultimo elemento de la lista de Ventas, y le sumo 1
def calcular_id():
    return int(elementos[len(elementos)-1][0]) + 1

def ingresar_productos_venta():
    ingreso = "1"
    productos = []
    while ingreso == "1":
        producto = input("Ingrese el codigo de producto: ").upper()
        cantidad = int(input("Ingrese la cantidad: "))
        productos.append([producto, cantidad])
        print("¿Desea cargar mas productos?")
        ingreso = input("1 para continuar, 0 para finalizar: ")
        while ingreso not in ("0", "1"):
            ingreso = input("Opción inválida. Ingrese 1 para continuar o 0 para finalizar: ")
    
    return productos
    
def crear_venta():
    
    mostrar_linea_divisoria(ancho_standard)
    print('Creacion de nueva venta')
    mostrar_linea_divisoria(ancho_standard)
    nombre_empleado = input("Ingrese el nombre del empleado: ")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    total_venta = float(input("Ingrese el total de la venta: "))
    fecha_venta = input("Ingrese la fecha en formato dd-MM-aaaa: ")
    productos = ingresar_productos_venta()
    venta = [calcular_id(), nombre_empleado, nombre_cliente, total_venta, fecha_venta, productos, True]
    elementos.append(venta)
    mostrar_linea_divisoria(ancho_standard)
    print(f"Venta creada con Id: {AMARILLO}{venta[ID]}")
    mostrar_linea_divisoria(ancho_standard)

def obtener_venta():
    mostrar_linea_divisoria(ancho_standard)
    print("Busqueda de Venta por ID")
    mostrar_linea_divisoria(ancho_standard)
    id = input("Ingrese el Id de la venta: ")
    venta = obtener_venta_por_id(id)
    if venta is None:
        return
    mostrar_linea_divisoria(ancho_standard)
    mostrar_venta(venta)
    mostrar_linea_divisoria(ancho_standard)


def obtener_venta_por_id(id):

    encontre = False
    i = 0
    venta = []
    while not encontre and i < len(elementos):
        if id == str(elementos[i][ID]) and elementos[i][ACTIVO]:
            venta = elementos[i]
            encontre = True
        i += 1
    if venta == []:
        mostrar_linea_divisoria(ancho_standard)
        print(f"No existe la venta con id: {AMARILLO}{id}")
        mostrar_linea_divisoria(ancho_standard)
        return
    else:
        return venta

        
def actualizar_venta():
    mostrar_linea_divisoria(ancho_standard)
    print("Actualizacion de venta")
    mostrar_linea_divisoria(ancho_standard)
    id = input("Ingrese el Id a actualizar: ")
    venta = obtener_venta_por_id(id)

    if venta is None:
        return

    print("Ingrese los nuevos valores para:")
    mostrar_venta(venta)
    print()
    venta[VENDEDOR] = input("Ingrese el nombre del empleado: ")
    venta[CLIENTE] = input("Ingrese el nombre del cliente: ")
    venta[TOTAL_VENTA] = float(input("Ingrese el total de la venta: "))
    venta[FECHA] = input("Ingrese la fecha en formato dd-MM-aaaa: ")
    venta[ARTICULOS] = ingresar_productos_venta()
    mostrar_linea_divisoria(ancho_standard)
    print('Venta actualizada:')
    mostrar_venta(venta)
    mostrar_linea_divisoria(ancho_standard)

def eliminar_venta():
    mostrar_linea_divisoria(ancho_standard)
    print("Eliminacion de Venta")
    mostrar_linea_divisoria(ancho_standard)
    id = input("Igrese el Id a eliminar: ")
    venta = obtener_venta_por_id(id)
    if venta is None:
        return
    
    venta[ACTIVO] = False
    mostrar_linea_divisoria(ancho_standard)
    print(f"Venta eliminada con Id: {ROJO}{venta[ID]}")
    mostrar_linea_divisoria(ancho_standard)

def mostrar_ventas():
    """
    Metodo para mostrar las ventas utilizando ANSI
    """
    while True:
        mostrar_linea_divisoria(ancho_standard)
        print("Visualizacion de Ventas")
        mostrar_linea_divisoria(ancho_standard)
        print(
            f"{BOLD}"
            f"{encabezados[ID]:<4} | "
            f"{encabezados[VENDEDOR]:<25} | "
            f"{encabezados[CLIENTE]:<20} | "
            f"{encabezados[TOTAL_VENTA]:<11} | "
            f"{encabezados[FECHA]:<12} | "
            f"{encabezados[ARTICULOS]:<30}"
            f"{RESET}"
        )
        mostrar_linea_divisoria(ancho_standard)

        ventas = list(filter(lambda x: x[ACTIVO] is True, elementos))

        for venta in ventas:
            articulos_str = ", ".join([f"{cod}({cant})" for cod, cant in venta[ARTICULOS]])
            print(
                f'{AMARILLO}{venta[ID]:<4}{RESET} | '
                f'{venta[VENDEDOR]:<25.25} | '
                f'{venta[CLIENTE]:<20.20} | '
                f'${venta[TOTAL_VENTA]:<10.2f} | '
                f'{venta[FECHA]:<12} | '
                f'{CYAN}{articulos_str:<30.30}{RESET}'
            )

        print()
        sort = input("Ingrese 1 ordenar por Fecha, 2 por Monto, 3 por Vendedor, 0 para terminar: ")
        if sort == "0":
            elementos.sort(key=lambda x: int(str(x[ID])))
            mostrar_linea_divisoria(ancho_standard)
            return
        if sort == "1":
            elementos.sort(key=lambda x: x[FECHA])
        elif sort == "2":
            elementos.sort(key=lambda x: x[TOTAL_VENTA])
        elif sort == "3":
            elementos.sort(key=lambda x: x[VENDEDOR])
        else:
            input("Opción inválida. Presione ENTER para continuar.")


