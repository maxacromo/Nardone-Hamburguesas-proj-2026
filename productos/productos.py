RESET = "\033[0m"
BOLD = "\033[1m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
CYAN = "\033[36m"
BOLD_VERDE = "\033[1;32m"

combo1 = {"pan", "carne"}
combo2 = {"pan", "carne", "queso"}
combo3 = {"pan", "carne", "queso", "lechuga", "tomate"}
combo4 = {"pan", "carne", "queso", "bacon"}

productos = [
    (1, "Hamburguesa simple", 8000, combo1),
    (2, "Hamburguesa con queso", 10000, combo2),
    (3, "Hamburguesa completa", 12000, combo3),
    (4, "Hamburguesa bacon", 14000, combo4),
]


ANCHO_LINEA = 100


def linea_divisoria():
    print(f"{AZUL}{'-' * ANCHO_LINEA}{RESET}")


def crear_productos():
    return list(productos)


def mostrar_productos(lista=None):
    encabezados = ["Codigo", "Nombre", "Precio", "Ingredientes"]

    linea_divisoria()
    print(f"{BOLD}Lista de productos{RESET}")
    print()
    print(
        f"{BOLD}"
        f"{encabezados[0]:<8} | "
        f"{encabezados[1]:<26} | "
        f"{encabezados[2]:<13} | "
        f"{encabezados[3]:<44}"
        f"{RESET}"
    )
    linea_divisoria()

    for p in lista if lista is not None else productos:
        print(
            f"{AMARILLO}{str(p[0]):<8}{RESET} | "
            f"{(str(p[1])[:23] + '...') if len(str(p[1])) > 26 else str(p[1]):<26} | "
            f"{('$' + format(float(p[2]), '.2f')):<13} | "
            f"{CYAN}{(lambda s: s[:41] + '...' if len(s) > 44 else s)(', '.join(sorted(p[3]))):<44}{RESET}"
        )
    linea_divisoria()


def mostrar_productos(elementos):
    encabezados = ["Codigo", "Nombre", "Precio", "Cantidad", "Ingredientes"]

    print()
    print(f"{BOLD}Productos{RESET}")
    print(
        f"{BOLD}"
        f"{encabezados[0]:<8} | "
        f"{encabezados[1]:<26} | "
        f"{encabezados[2]:<13} | "
        f"{encabezados[3]:<10} | "
        f"{encabezados[4]:<44}"
        f"{RESET}"
    )
    linea_divisoria()

    for id, cant in elementos:
        producto = next((p for p in productos if p[0] == id), None)
        if producto is None:
            print(f"Producto con id {id} no encontrado")
            continue
        print(
            f"{AMARILLO}{str(producto[0]):<8}{RESET} | "
            f"{(str(producto[1])[:23] + '...') if len(str(producto[1])) > 26 else str(producto[1]):<26} | "
            f"{('$' + format(float(producto[2]), '.2f')):<13} | "
            f"{str(cant):<10} | "
            f"{CYAN}{(lambda s: s[:41] + '...' if len(s) > 44 else s)(', '.join(sorted(producto[3]))):<44}{RESET}"
        )


def comprar():
    carrito = []
    total_final = 0.0

    while True:
        codigo = int(input("\nIngrese código (0 para terminar): "))

        if codigo == 0:
            break

        cantidad = int(input("Cantidad: "))

        encontrado = False

        for p in productos:
            if p[0] == codigo:
                total = p[2] * cantidad
                carrito.append([p[1], p[2], cantidad, total, p[0]])
                total_final += total
                encontrado = True

        if not encontrado:
            print("Producto no encontrado")

    return carrito, total_final


def mostrar_carrito(carrito):
    linea_divisoria()
    print(f"{BOLD}Carrito de compras{RESET}")
    linea_divisoria()

    if not carrito:
        print(f"{AMARILLO}(sin ítems){RESET}")
        linea_divisoria()
        return

    encabezados = ["Producto", "P. unit.", "Cant.", "Subtotal"]
    print(
        f"{BOLD}"
        f"{encabezados[0]:<32} | "
        f"{encabezados[1]:>12} | "
        f"{encabezados[2]:>6} | "
        f"{encabezados[3]:>12}"
        f"{RESET}"
    )
    linea_divisoria()

    total_final = 0.0
    for item in carrito:
        nombre, p_unit, cant, sub = item[0], item[1], item[2], item[3]
        nombre_str = str(nombre)
        if len(nombre_str) > 32:
            nombre_str = nombre_str[:29] + "..."
        print(
            f"{AMARILLO}{nombre_str:<32}{RESET} | "
            f"${float(p_unit):>11} | "
            f"{int(cant):>6} | "
            f"{CYAN}${float(sub):>11}{RESET}"
        )
        total_final += float(sub)

    linea_divisoria()
    print(f"{BOLD}TOTAL:{RESET} {BOLD_VERDE}${total_final:.2f}{RESET}")
    linea_divisoria()


def eliminar_producto(productos):
    codigo = int(input("Ingrese código de producto a eliminar: "))

    producto_a_eliminar = None

    for p in productos:
        if p[0] == codigo:
            producto_a_eliminar = p

    if producto_a_eliminar:
        productos.remove(producto_a_eliminar)
        print("Producto eliminado")
    else:
        print("Producto no encontrado")
