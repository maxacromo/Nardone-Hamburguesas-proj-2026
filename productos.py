def crear_productos():
    combo1 = {"pan", "carne"}
    combo2 = {"pan", "carne", "queso"}
    combo3 = {"pan", "carne", "queso", "lechuga", "tomate"}
    combo4 = {"pan", "carne", "queso", "bacon"}

    productos = [
        (1, "Hamburguesa simple", 8000, combo1),
        (2, "Hamburguesa con queso", 10000, combo2),
        (3, "Hamburguesa completa", 12000, combo3),
        (4, "Hamburguesa bacon", 14000, combo4)
    ]

    return productos

def mostrar_productos(productos):
    print("\nLista de productos:\n")

    for p in productos:
        ingredientes = ", ".join(p[3])
        print(f"{p[0]} - {p[1]} - ${p[2]}")
        print(f"   Ingredientes: {ingredientes}")

def comprar(productos):
    carrito = []

    while True:
        codigo = int(input("\nIngrese código (0 para terminar): "))

        if codigo == 0:
            break

        cantidad = int(input("Cantidad: "))

        encontrado = False

        for p in productos:
            if p[0] == codigo:
                total = p[2] * cantidad
                carrito.append([p[1], p[2], cantidad, total])
                encontrado = True

        if not encontrado:
            print("Producto no encontrado")

    return carrito

def mostrar_carrito(carrito):
    print("\nCarrito:\n")
    total_final = 0

    for item in carrito:
        print(f"{item[0]} - ${item[1]} x {item[2]} = ${item[3]}")
        total_final += item[3]

    print(f"\nTOTAL: ${total_final}")


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

