from .constantes import *

encabezados = ['Nro de Venta', 'Empleado', 'Cliente', 'Total', 'Fecha' ,'Articulos']
elementos = [
    ['1', 'Ezequiel Gonzalez', 'Juan Perez', 100, '31-01-2026', [['A001', 1], ['A002', 2]]],
    ['2', 'Ezequiel Gonzalez', 'Pepe Alvarez', 130, '02-02-2026', [['A003', 1], ['A004', 1]]],
    ['3', 'Ezequiel Gonzalez', 'Pedro Lopez', 105, '06-02-2026', [['A001', 1], ['A005', 1]]],
    ['4', 'Juan Perez', 'Pedro Lopez', 1052, '01-03-2026', [['A006', 2], ['A007', 3]]],
    ['5', 'Juan Perez', 'Pedro Lopez', 2050, '01-03-2026', [['A008', 1], ['A009', 5]]],
    ['6', 'Juan Perez', 'Pedro Lopez', 500, '01-03-2026', [['A002', 4], ['A010', 1]]],
    ['7', 'Maria Lopez', 'Carlos Diaz', 890, '05-03-2026', [['A003', 2], ['A004', 3]]],
    ['8', 'Maria Lopez', 'Ana Torres', 450, '05-03-2026', [['A005', 1], ['A001', 2]]],
    ['9', 'Lucas Fernandez', 'Juan Perez', 1200, '10-03-2026', [['A011', 2], ['A012', 1]]],
    ['10', 'Lucas Fernandez', 'Sofia Gomez', 750, '10-03-2026', [['A007', 1], ['A003', 2]]],
    ['11', 'Ezequiel Gonzalez', 'Lucia Martinez', 320, '12-03-2026', [['A002', 2], ['A006', 1]]],
    ['12', 'Juan Perez', 'Diego Suarez', 980, '15-03-2026', [['A009', 2], ['A001', 3]]],
    ['13', 'Maria Lopez', 'Valentina Ruiz', 1500, '16-03-2026', [['A010', 1], ['A011', 2]]],
    ['14', 'Lucas Fernandez', 'Martin Acosta', 670, '18-03-2026', [['A004', 2], ['A008', 1]]],
    ['15', 'Ezequiel Gonzalez', 'Camila Benitez', 430, '20-03-2026', [['A003', 1], ['A005', 2]]],
    ['16', 'Juan Perez', 'Fernando Silva', 2500, '22-03-2026', [['A012', 4], ['A006', 2]]],
    ['17', 'Maria Lopez', 'Pedro Lopez', 300, '22-03-2026', [['A001', 1], ['A007', 1]]],
    ['18', 'Lucas Fernandez', 'Juan Perez', 1100, '25-03-2026', [['A009', 2], ['A010', 2]]],
    ['19', 'Ezequiel Gonzalez', 'Pepe Alvarez', 870, '27-03-2026', [['A002', 3], ['A011', 1]]],
    ['20', 'Juan Perez', 'Carlos Diaz', 1990, '28-03-2026', [['A008', 2], ['A012', 3]]]
]




# Para calcular el Id, obtengo el Id del ultimo elemento de la lista de Ventas, y le sumo 1
def calcular_id():
    return int(elementos[len(elementos)-1][0]) + 1
    
def crear_venta():
    nombre_empleado = input("Ingrese el nombre del empleado: ")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    total_venta = float(input("Ingrese el total de la venta: "))
    venta = [calcular_id(), nombre_empleado, nombre_cliente, total_venta]
    elementos.append(venta)

def obtener_venta(id):

    encontre = False
    i = 0
    venta = []
    while(not encontre & i < len(elementos)):
        if str(id) == elementos[i][ID]:
            venta = elementos[i]
            encontre = True
        i += 1
    if venta == []:
        print("No existe la venta con id: ", id)
        return
    else:
        return venta

        
def actualizar_venta():
    id = input("Igrese el Id a actualizar: ")
    venta = obtener_venta(id)

    if venta is None:
        return

    print("Ingrese los nuevos valores para: ", venta)
    venta[VENDEDOR] = input("Ingrese el nombre del empleado: ")
    venta[CLIENTE] = input("Ingrese el nombre del cliente: ")
    venta[TOTAL_VENTA] = float(input("Ingrese el total de la venta: "))

def eliminar_venta():
    id = input("Igrese el Id a eliminar: ")
    venta = obtener_venta(id)
    if venta is None:
        return
    
    elementos.remove(venta)

def obtener_ventas_por_fecha(fecha):
    ventas = [v for v in elementos if fecha == v[FECHA]]
    return ventas

def mostrar_encabezados():
    for encabezado in encabezados:
        print(encabezado, end="\t\t")
    print()

def mostrar_elementos():
    for elemento in elementos:
        for x in elemento:
            print(x, end="\t\t")
        print()

def mostrar_ventas():
    mostrar_encabezados()
    mostrar_elementos()

