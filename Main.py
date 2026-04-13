from modelo_stock import stock
from Vista_stock import inicio_stock
from Controlador_stock import *

def menu():
    opcion = ""

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

menu()