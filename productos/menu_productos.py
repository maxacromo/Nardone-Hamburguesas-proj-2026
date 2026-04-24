from productos.productos import crear_productos, mostrar_productos, comprar, eliminar_producto

ancho_menu = 100

def menu_productos():
    productos = crear_productos()

    while True:
        print("-"*ancho_menu)
        print("MENÚ PRINCIPAL > MENÚ DE PRODUCTOS")
        print("-"*ancho_menu)
        print("[1] Mostrar productos")
        print("[2] Eliminar producto")
        print("-"*ancho_menu)
        print("[0] Salir")
        print("-"*ancho_menu)

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            mostrar_productos(productos)

        elif opcion == "2":
            eliminar_producto(productos)

        elif opcion == "0":
            break

        else:
            print("Opción inválida")


#productos = crear_productos()
#mostrar_productos(productos)
#carrito, total_final = comprar()



