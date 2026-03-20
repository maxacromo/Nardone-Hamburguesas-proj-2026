encabezados = ['Nro de Venta', 'Empleado', 'Cliente', 'Total']
elementos = [
    ['1', 'Ezequiel Gonzalez', 'Juan Perez', 100], 
    ['2', 'Ezequiel Gonzalez', 'Pepe Alvarez', 130], 
    ['3', 'Ezequiel Gonzalez', 'Pedro Lopez', 105]]

def mostrar_encabezados():
    for encabezado in encabezados:
        print(encabezado, end="\t\t")
    print()

def mostrar_elementos():
    for elemento in elementos:
        for x in elemento:
            print(x, end="\t\t")
        print()

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
    for e in elementos:
        if str(id) == e[0]:
            return e
    print("No existe la venta con id: ", id)
    return
        
def actualizar_venta():
    id = input("Igrese el Id a actualizar: ")
    venta = obtener_venta(id)

    if venta is None:
        return

    print("Ingrese los nuevos valores para: ", venta)
    venta[1] = input("Ingrese el nombre del empleado: ")
    venta[2] = input("Ingrese el nombre del cliente: ")
    venta[3] = float(input("Ingrese el total de la venta: "))

def eliminar_venta():
    id = input("Igrese el Id a eliminar: ")
    venta = obtener_venta(id)
    if venta is None:
        return
    
    elementos.remove(venta)

def mostrar_ventas():
    mostrar_encabezados()
    mostrar_elementos()

mostrar_ventas()
eliminar_venta()
mostrar_ventas()

