from .constantes import *
from productos.productos import comprar, mostrar_productos, mostrar_carrito, mostrar_productos, mostrar_productos_de_venta, crear_productos
from empleados.utils import obtener_nombre_apellido
from Clientes.Clientes import buscar_o_crear_cliente, cargar_clientes
import re
import csv
import os

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

CSV_PATH = os.path.join(os.path.dirname(__file__), 'ventas_historico.csv')

def articulos_a_str(articulos):
    return ";".join(f"{cod}:{cant}" for cod, cant in articulos)

def str_a_articulos(texto):
    return [[p.split(":")[0], int(p.split(":")[1])] for p in texto.split(";") if p]

def cargar_ventas():
    ventas = []
    try:
        with open(CSV_PATH, newline='', encoding='UTF-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                ventas.append([
                    row['id'],
                    row['empleado'],
                    row['cliente'],
                    float(row['total']),
                    row['fecha'],
                    str_a_articulos(row['articulos']),
                    row['activo'] == 'True'
                ])
    except (FileNotFoundError, OSError) as error:
        print("Error al cargar ventas:", error)
    return ventas

def guardar_ventas(ventas):
    try:
        with open(CSV_PATH, 'w', newline='', encoding='UTF-8') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'empleado', 'cliente', 'total', 'fecha', 'articulos', 'activo'])
            for v in ventas:
                writer.writerow([v[ID], v[VENDEDOR], v[CLIENTE], v[TOTAL_VENTA], v[FECHA], articulos_a_str(v[ARTICULOS]), v[ACTIVO]])
    except (FileNotFoundError, OSError) as error:
        print("Error al guardar ventas:", error)

elementos = cargar_ventas()

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
    mostrar_productos_de_venta(venta[ARTICULOS])


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

def obtener_productos_carrito(carrito):
    """
    Convierte el carrito del formato
    [nombre, precio_unit, cantidad, subtotal, codigo_producto]
    en la lista de artículos de la venta: [[codigo_producto, cantidad], ...].
    """
    if not carrito:
        return []
    resultado = []
    for item in carrito:
        if len(item) < 5:
            continue
        codigo, cantidad = item[4], item[2]
        resultado.append([codigo, cantidad])
    return resultado


def crear_venta(usuario):

    productos = crear_productos()
    mostrar_linea_divisoria(ancho_standard)
    print('Creacion de nueva venta')
    mostrar_productos(productos)
    carrito, total_final = comprar()
    mostrar_carrito(carrito)
    productos_venta = obtener_productos_carrito(carrito)

    personas_id, clientes, mail_list = cargar_clientes()
    id_cliente = buscar_o_crear_cliente(personas_id, clientes, mail_list, ["yes","y","no","n"])

    patron_fecha = r"^(0[1-9]|[12]\d|3[01])-(0[1-9]|1[0-2])-\d{4}$"
    while True:
        fecha_venta = input("Ingrese la fecha en formato dd-MM-aaaa: ")
        if re.match(patron_fecha, fecha_venta):
            break
        print("Fecha inválida. Asegúrese de usar el formato dd-MM-aaaa (ej: 25-03-2025)")

    nombre = obtener_nombre_apellido(usuario)
    venta = [calcular_id(), nombre, id_cliente, total_final, fecha_venta, productos_venta, True]
    elementos.append(venta)
    guardar_ventas(elementos)
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

    patron_fecha = r"^(0[1-9]|[12]\d|3[01])-(0[1-9]|1[0-2])-\d{4}$"
    while True:
        fecha_venta = input("Ingrese la fecha en formato dd-MM-aaaa: ")
        if re.match(patron_fecha, fecha_venta):
            break
        print("Fecha inválida. Asegúrese de usar el formato dd-MM-aaaa (ej: 25-03-2025)")

    venta[ARTICULOS] = ingresar_productos_venta()
    guardar_ventas(elementos)
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
    guardar_ventas(elementos)
    mostrar_linea_divisoria(ancho_standard)
    print(f"Venta eliminada con Id: {ROJO}{venta[ID]}")
    mostrar_linea_divisoria(ancho_standard)

def resolver_nombre_cliente(id_cliente, clientes):
    key = str(id_cliente)
    if key in clientes:
        return clientes[key][0]
    return str(id_cliente)

def mostrar_ventas():
    """
    Metodo para mostrar las ventas utilizando ANSI
    """
    _, clientes, _ = cargar_clientes()
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
            nombre_cliente = resolver_nombre_cliente(venta[CLIENTE], clientes)
            print(
                f'{AMARILLO}{venta[ID]:<4}{RESET} | '
                f'{venta[VENDEDOR]:<25.25} | '
                f'{nombre_cliente:<20.20} | '
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


def buscar_ventas_por_cliente():
    from Clientes.Clientes import buscar_cliente_by_user
    mostrar_linea_divisoria(ancho_standard)
    print("Historial de compras por cliente")
    mostrar_linea_divisoria(ancho_standard)

    usuario = input("Ingrese el usuario del cliente: ").strip()
    try:
        id_cliente = buscar_cliente_by_user(usuario)
    except (ValueError, TypeError):
        print(f"No existe ningún cliente con usuario '{usuario}'.")
        mostrar_linea_divisoria(ancho_standard)
        return

    _, clientes, _ = cargar_clientes()
    nombre_cliente = resolver_nombre_cliente(id_cliente, clientes)

    ventas_cliente = [v for v in elementos if str(v[CLIENTE]) == str(id_cliente) and v[ACTIVO]]

    mostrar_linea_divisoria(ancho_standard)
    if not ventas_cliente:
        print(f"No se encontraron ventas para el cliente '{nombre_cliente}'.")
        mostrar_linea_divisoria(ancho_standard)
        return

    print(f"Ventas de: {AMARILLO}{nombre_cliente}{RESET}")
    mostrar_linea_divisoria(ancho_standard)
    print(
        f"{BOLD}"
        f"{encabezados[ID]:<4} | "
        f"{encabezados[VENDEDOR]:<25} | "
        f"{encabezados[TOTAL_VENTA]:<11} | "
        f"{encabezados[FECHA]:<12} | "
        f"{encabezados[ARTICULOS]:<30}"
        f"{RESET}"
    )
    mostrar_linea_divisoria(ancho_standard)

    total_gastado = 0
    for venta in ventas_cliente:
        articulos_str = ", ".join([f"{cod}({cant})" for cod, cant in venta[ARTICULOS]])
        print(
            f'{AMARILLO}{venta[ID]:<4}{RESET} | '
            f'{venta[VENDEDOR]:<25.25} | '
            f'${venta[TOTAL_VENTA]:<10.2f} | '
            f'{venta[FECHA]:<12} | '
            f'{CYAN}{articulos_str:<30.30}{RESET}'
        )
        total_gastado += venta[TOTAL_VENTA]

    mostrar_linea_divisoria(ancho_standard)
    print(f"Total de compras: {BOLD_VERDE}{len(ventas_cliente)}{RESET}  |  Total gastado: {BOLD_VERDE}${total_gastado:.2f}{RESET}")
    mostrar_linea_divisoria(ancho_standard)

