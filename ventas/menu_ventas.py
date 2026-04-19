
from ventas.ventas import mostrar_ventas, crear_venta, actualizar_venta, eliminar_venta, obtener_venta, elementos
from ventas.estadisticas import obtener_ventas_por_cada_vendedor, obtener_articulo_mas_vendido, obtener_cant_total_ventas

ancho_menu = 100
def mostrar_menu_ventas(empleado_logueado):

    while True:
        opciones = 5
        print("-"*ancho_menu)
        print("MENÚ PRINCIPAL > MENÚ DE VENTAS")
        print("-"*ancho_menu)
        print("[1] Visualizar Ventas")
        print("[2] Crear Venta")
        print("[3] Editar Venta")
        print("[4] Eliminar Venta")
        print("[5] Buscar Venta por ID")
        print("-"*ancho_menu)
        print("[0] Volver al menú anterior")
        print("-"*ancho_menu)
        print()

        opcion = input("Seleccione una opción: ")
        if opcion not in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
            input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0": # Opción salir del submenú
            break # No salimos del programa, volvemos al menú anterior
        elif opcion == "1":
            mostrar_ventas()
        elif opcion == "2":
            crear_venta(empleado_logueado)
        elif opcion == "3":
            actualizar_venta()
        elif opcion == "4":
            eliminar_venta()
        elif opcion == "5":
            obtener_venta()

def mostrar_menu_estadisticas():

    while True:
        opciones = 5
        print("-"*ancho_menu)
        print("MENÚ PRINCIPAL > MENÚ DE ESTADISTICAS")
        print("-"*ancho_menu)
        print("[1] Obtener ventas de cada vendedor")
        print("[2] Obtener el articulo mas vendido")
        print("[3] Ver la cantidad total de ventas")
        print("-"*ancho_menu)
        print("[0] Volver al menú anterior")
        print("-"*ancho_menu)
        print()

        opcion = input("Seleccione una opción: ")
        if opcion not in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
            input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0": # Opción salir del submenú
            break # No salimos del programa, volvemos al menú anterior
        elif opcion == "1":
            obtener_ventas_por_cada_vendedor(elementos)
        elif opcion == "2":
            obtener_articulo_mas_vendido(elementos)
        elif opcion == "3":
            obtener_cant_total_ventas(elementos)



      