import json
import os
from stock.Vista_stock import inicio_stock
from stock.modelo_stock import stock

RUTA_JSON = os.path.join(os.path.dirname(__file__), "modelo_stock.json")

def cargar_stock_json():
    try:
        with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("El archivo no se puede encontrar.")
        return None
def guardar_stock_json(diccionario_stock):
    try:
        with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
            json.dump(diccionario_stock, archivo, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        print("El archivo no se puede encontrar para guardar los datos.")

def anadir_ingrediente(stock):
    nombre = input("Ingrese el nombre del nuevo ingrediente: ").strip()
    while nombre == "":
        nombre = input("El nombre no puede estar vacio. Ingrese el nombre del nuevo ingrediente: ").strip()
    while not nombre.replace(" ", "").isalpha():
        print("El nombre ingresado no es una palabra")
        nombre = input("Ingrese el nombre del nuevo ingrediente: ").strip()
        
    for ingrediente_existente in stock.keys():
        if ingrediente_existente.lower() == nombre.lower():
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
            
    stock[nombre] = cantidad
    guardar_stock_json(stock) 
    print("El nuevo ingrediente ha sido agregado.")
    
def borrar_ingrediente(stock):
    nombre = input("Ingrese el nombre del ingrediente que desea borrar: ").strip()
    while nombre == "":
        nombre = input("El nombre no puede estar vacio. Ingrese el nombre del nuevo ingrediente: ").strip()
        
    llave_a_borrar = None
    for ingrediente in stock.keys():
        if ingrediente.lower() == nombre.lower():
            llave_a_borrar = ingrediente
            break
            
    if llave_a_borrar:
        stock.pop(llave_a_borrar) 
        guardar_stock_json(stock) 
        print("Ingrediente Eliminado")
    else:
        print("Ingrediente no encontrado")

def modificar_ingrediente(stock):
    nombre = input("Ingrese el nombre del ingrediente que desea modificar el stock: ").strip()
    while nombre == "":
        nombre = input("El nombre no puede estar vacio. Ingrese el nombre del ingrediente que desea modificar el stock: ").strip()

    llave_a_modificar = None
    for ingrediente in stock.keys():
        if ingrediente.lower() == nombre.lower():
            llave_a_modificar = ingrediente
            break

    if llave_a_modificar:
        while True:
            cantidad_str = input("Ingrese la cantidad de stock del nuevo ingrediente: ")
            if not cantidad_str.isdigit():
                print("El valor ingresado no es un numero entero")
            elif int(cantidad_str) <= 0:
                print("Se tiene que ingresar un stock mayor a 0.")
            else:
                nuevo_stock = int(cantidad_str)
                break
                
        stock[llave_a_modificar] = nuevo_stock 
        guardar_stock_json(stock) 
        print("El stock se actualizo")
    else:
        print("No se encontro el ingrediente")
        
def listar_stock(stock):
    print("\n---Stock Actual ---")
    if not stock:
        print("(No hay ingredientes cargados en el sistema porque el archivo no se encontró)")
        return
        
    for ingrediente, cantidad in stock.items():
        print(f"{ingrediente}: {cantidad}")
        
def buscar_por_nombre(stock):
    nombre = input("Ingrese el nombre del ingrediente que desea buscar: ").strip()
    while nombre == "":
        nombre = input("El nombre no puede estar vacio. Ingrese el ingrediente que desea buscar: ").strip()
        
    for ingrediente, cantidad in stock.items():
        if ingrediente.lower() == nombre.lower():
            print(f"{ingrediente}: {cantidad}")
            return
    print("No se encontro el producto")

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
