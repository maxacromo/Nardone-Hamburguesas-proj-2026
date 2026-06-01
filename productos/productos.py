from stock.Controlador_stock import cargar_stock_json, guardar_stock_json

RESET = "\033[0m"
BOLD = "\033[1m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
CYAN = "\033[36m"
BOLD_VERDE = "\033[1;32m"

receta_simple = {"Pan": 2, "Carne": 1}
receta_queso = {"Pan": 2, "Carne": 1, "Queso": 1}
receta_completa = {"Pan": 2, "Carne": 1, "Queso": 1, "Lechuga": 1, "Tomate": 1, "Cebolla": 1}
receta_bacon = {"Pan": 2, "Carne": 1, "Queso": 1, "Bacon": 1}

productos = [
    (1, "Hamburguesa simple", 8000, receta_simple),
    (2, "Hamburguesa con queso", 10000, receta_queso),
    (3, "Hamburguesa completa", 12000, receta_completa),
    (4, "Hamburguesa bacon", 14000, receta_bacon),
]



ANCHO_LINEA = 100


def linea_divisoria():
    print(f"{AZUL}{'-' * ANCHO_LINEA}{RESET}")

def linea_divisoria_con_ancho(ancho):
    print(f"{AZUL}{'-' * ancho}{RESET}")


def crear_productos():
    return list(productos)

def mostrar_productos_de_venta(lista):
    encabezados = ["Codigo", "Nombre", "Precio", "Ingredientes", "Cantidad"]

    linea_divisoria_con_ancho(115)
    print(f"{BOLD}Lista de productos{RESET}")
    print()
    print(
        f"{BOLD}"
        f"{encabezados[0]:<8} | "
        f"{encabezados[1]:<26} | "
        f"{encabezados[2]:<13} | "
        f"{encabezados[3]:<44} | "
        f"{encabezados[4]:<8}"
        f"{RESET}"
    )
    linea_divisoria_con_ancho(115)

    cantidad_por_id = {int(item[0]): item[1] for item in lista}
    ids = cantidad_por_id.keys()
    prods_a_mostrar = [(prod, cantidad_por_id[prod[0]]) for prod in productos if prod[0] in ids]

    for prod, cantidad in prods_a_mostrar:
        print(
            f"{AMARILLO}{str(prod[0]):<8}{RESET} | "
            f"{(str(prod[1])[:23] + '...') if len(str(prod[1])) > 26 else str(prod[1]):<26} | "
            f"{('$' + format(float(prod[2]), '.2f')):<13} | "
            f"{CYAN}{(lambda s: s[:41] + '...' if len(s) > 44 else s)(', '.join(sorted(prod[3]))):<44}{RESET} | "
            f"{str(cantidad):<8}"
        )
    linea_divisoria_con_ancho(115)


def mostrar_productos(lista):
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

    for prod in lista:
        print(
            f"{AMARILLO}{str(prod[0]):<8}{RESET} | "
            f"{(str(prod[1])[:23] + '...') if len(str(prod[1])) > 26 else str(prod[1]):<26} | "
            f"{('$' + format(float(prod[2]), '.2f')):<13} | "
            f"{CYAN}{(lambda s: s[:41] + '...' if len(s) > 44 else s)(', '.join(sorted(prod[3]))):<44}{RESET}"
        )
    linea_divisoria()


def mostrar_productos_seleccionados(elementos):
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

def actualizar_stock(receta, cantidad, modo):
    stock = cargar_stock_json()
    
    if stock is not None: 
        for ingrediente_nombre, cant_unitaria in receta.items():
            if ingrediente_nombre in stock:
                if modo == "restar":
                    stock[ingrediente_nombre] -= (cant_unitaria * cantidad)
                elif modo == "sumar":
                    stock[ingrediente_nombre] += (cant_unitaria * cantidad)
        
        guardar_stock_json(stock)

def comprar():
    carrito = []
    total_final = 0.0

    while True:
        codigo = int(input("\nIngrese código (0 para terminar): "))

        if codigo == 0:
            break

        cantidad = int(input("Cantidad: "))

        encontrado = None
        for p in productos:
            if p[0] == codigo:
                encontrado = p

        if encontrado:
            actualizar_stock(encontrado[3], cantidad, "restar")
            total = encontrado[2] * cantidad
            
            carrito.append([encontrado[1], encontrado[2], cantidad, total, codigo])
            total_final += total
            print(f"{encontrado[1]} agregado al carrito.")
        else:
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


def eliminar_producto(carrito):
    codigo = int(input("Ingrese código de producto a eliminar: "))

    producto_a_eliminar = None
    
    for p in productos:
        if p[4] == codigo:
            producto_a_eliminar = p
            break

    if producto_a_eliminar:
        receta_para_devolver = None
        for prod in productos:
            if prod[0] == codigo:
                receta_para_devolver = prod[3]
                break
            
        if receta_para_devolver:
            cantidad_comprada = producto_a_eliminar[2]
            actualizar_stock(receta_para_devolver, cantidad_comprada, "sumar")
            
        carrito.remove(producto_a_eliminar)
        print("Producto eliminado")
    else:
        print("Producto no encontrado")
