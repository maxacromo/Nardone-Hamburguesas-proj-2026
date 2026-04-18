from productos import crear_productos, mostrar_productos, comprar, mostrar_carrito, eliminar_producto

def menu():
    productos = crear_productos()

    while True:
        print("\n--- MENÚ ---")
        print("1. Mostrar productos")
        print("2. Comprar")
        print("3. Eliminar producto")
        print("0. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            mostrar_productos(productos)

        elif opcion == "2":
            carrito = comprar(productos)
            mostrar_carrito(carrito)

        elif opcion == "3":
            eliminar_producto(productos)

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")

productos = crear_productos()
mostrar_productos(productos)
carrito = comprar(productos)



