
stock= [
    ["Hamburguesa", 500],
    ["Queso", 300],
    ["Tomate", 100],
    ["Lechuga",100],
    ["Pan", 1000],
    ["Cebolla", 100]
]

def inicio_stock():
    print("\n---Administracion de stock ---")
    print("1. Añadir nuevo ingrediente")
    print("2. Borrar ingrediente")
    print("3. Modificar stock de un ingrediente")
    print("4. Listar ingredientes")
    print("5. Buscar ingrediente en stock")
    print("0. Salir")
    
    
def anadir_ingrediente(stock):
    nombre= input("Ingrese el nombre del nuevo ingrediente:").strip()
    while nombre == "":
        nombre= input("El nombre no puede estar vacio. Ingrese el nombre del nuevo ingrediente:").strip()
    for ingrediente in stock:
        if ingrediente[0].lower() == nombre.lower():
            print("El ingrediente ya esta cargado.")
            return
    cantidad= int(input("Ingrese la cantidad de stock del nuevo ingrediente: "))
    while cantidad <= 0:
        cantidad= int(input("Se tiene que ingresar un stock mayor a 0. Ingrese la cantidad de stock del nuevo ingrediente:"))
    ingrediente= [nombre, cantidad]
    stock.append(ingrediente)
    print("El nuevo ingrediente ha sido agregado.")
    
def borrar_ingrediente(stock):
    nombre= input("Ingrese el nombre del ingrediente que desea borrar:").strip()
    while nombre == "":
        nombre= input("El nombre no puede estar vacio. Ingrese el nombre del nuevo ingrediente:").strip()
    for ingrediente in stock:
        if ingrediente[0] == nombre:
            stock.remove(ingrediente)
            print("Ingrediente Eliminado")
            return
    print("Ingrediente no encontrado")
    return

def modificar_ingrediente(stock):
    nombre= input("Ingrese el nombre del ingrediente que desea modificar el stock: ").strip()
    while nombre == "":
        nombre= input("El nombre no puede estar vacio.Ingrese el nombre del ingrediente que desea modificar el stock: ").strip()
    for ingrediente in stock:
        if ingrediente[0].lower() == nombre.lower():
            nuevo_stock= int(input("Ingrese el nuevo stock:"))
            while nuevo_stock < 0:
                nuevo_stock= int(input("El stock debe ser mayor que cero. Ingrese el nuevo stock:"))
            ingrediente[1]= nuevo_stock
            return
    print("No se encontro el ingrediente")
        
def listar_stock(stock):
    print("\n---Stock Actual ---")
    for ingrediente in stock:
        print(f"{ingrediente[0]}: {ingrediente[1]}")
        
def buscar_por_nombre(stock):
    nombre= input("Ingrese el ingrediente que desea buscar: ").strip()
    while nombre == "":
        nombre= input("El nombre no puede estar vacio. Ingrese el ingrediente que desea buscar: ").strip()
    for ingrediente in stock:
        if ingrediente[0].lower() == nombre.lower():
            print(f"{ingrediente[0]}: {ingrediente[1]}")
            return 
        
def adm_stock(stock):
    opcion= ''
    while opcion != "0":
        inicio_stock()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            anadir_ingrediente(stock)
        elif opcion == "2":
            borrar_ingrediente(stock)
        elif opcion == "3":
            modificar_ingrediente(stock)
        elif opcion == "4":
            listar_stock(stock)
        elif opcion == "5":
            buscar_por_nombre(stock)
        elif opcion == "0":
            break #Futuro return al menu

adm_stock(stock)