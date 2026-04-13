from modelo_stock import stock

def anadir_ingrediente(stock):
    nombre= input("Ingrese el nombre del nuevo ingrediente:").strip()
    while nombre == "":
        nombre= input("El nombre no puede estar vacio. Ingrese el nombre del nuevo ingrediente:").strip()
    while not nombre.replace(" ", "").isalpha():
        print("El nombre ingresado no es una palabra")
        nombre= input("Ingrese el nombre del nuevo ingrediente:").strip()
        
    for ingrediente in stock:
        if ingrediente[0].lower() == nombre.lower():
            print("El ingrediente ya esta cargado.")
            return
    while True:
        cantidad_str = input("Ingrese la cantidad de stock del nuevo ingrediente: ")
        if not cantidad_str.isdigit():
            print("El valor ingresado no es un numero entero")
        elif int(cantidad_str) < 0:
            print("Se tiene que ingresar un stock positivo.")
        else:
            cantidad = int(cantidad_str)
            break
    ingrediente= [nombre, cantidad]
    stock.append(ingrediente)
    print("El nuevo ingrediente ha sido agregado.")
    
def borrar_ingrediente(stock):
    nombre= input("Ingrese el nombre del ingrediente que desea borrar:").strip()
    while nombre == "":
        nombre= input("El nombre no puede estar vacio. Ingrese el nombre del nuevo ingrediente:").strip()
    for ingrediente in stock:
        if ingrediente[0].lower() == nombre.lower():
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
            while True:
                cantidad_str = input("Ingrese la cantidad de stock del nuevo ingrediente: ")
                if not cantidad_str.isdigit():
                    print("El valor ingresado no es un numero entero")
                elif int(cantidad_str) <= 0:
                    print("Se tiene que ingresar un stock mayor a 0.")
                else:
                    nuevo_stock = int(cantidad_str)
                    break
            ingrediente[1]= nuevo_stock
            print("El stock se actualizo")
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
    print("No se encontro el producto")
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
        else: 
            print("Opcion invalida")