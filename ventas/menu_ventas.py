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

def mostrar_menu():

    while True:
        opciones = 4
        print()
        print("---------------------------")
        print("MENÚ PRINCIPAL > MENÚ DE VENTAS")
        print("---------------------------")
        print("[1] Visualizar Ventas")
        print("[2] Crear Venta")
        print("[3] Editar Venta")
        print("[4] Eliminar Venta")
        print("---------------------------")
        print("[0] Volver al menú anterior")
        print("---------------------------")
        print()

        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
            break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")
    print()

def mostrar_productos(encabezados, elementos):
    ancho_total = 140

    print(f"{BOLD}{encabezados[0]:<8}{encabezados[1]:<25}{encabezados[2]:<25}{encabezados[3]:>10}{encabezados[4]:>15}{encabezados[5]:>25}{RESET}")
    print(f"{AZUL}{'-'*ancho_total}{RESET}")

    for venta in elementos:

        articulos_str = ", ".join([f"{cod}({cant})" for cod, cant in venta[5]])

        print(
            f'{AMARILLO}{venta[0]:<8}{RESET}'
            f'{venta[1]:<25}'
            f'{venta[2]:<25}'
            f'{venta[3]:>10.2f}'
            f'{venta[4]:>15}'
            f'{CYAN}{articulos_str:>25}{RESET}'
        )

    print(f"{AZUL}{'-'*ancho_total}{RESET}")            