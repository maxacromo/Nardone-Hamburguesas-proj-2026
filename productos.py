def crear_productos():
    productos= [
        [1, "hamburguesadoble con cheddar", 15000],
        [2, "hamburguesadoble con cheddar y panceta", 17000],
        [3, "papas sasonadas con cheddar", 8000],
        [4, "nuggest de pollo(10 unidades)", 10000],
        [5, "gaseosa/agua", 4000]
    ]
    return productos

def mostrar_productos(productos):
    print("\nLista de productos:")
    for p in productos:
        print(f"{p[0]} - {p[1]} - ${p[2]}")


def comprar(productos):
    carrito= []

    while True:
        codigo=int(input(" ingrese codigo de pruducto (0 par terminar)"))

        if codigo==0:
            break

        cantidad=int(input("cantidad: "))

        encontrado= False


        for p in productos:
            if p[0]==codigo:
                total=p[2]*cantidad
                carrito.append([p[1], p[2], cantidad, total])
                encontrado= True

        if not encontrado:
            print("ese producto no esta")

    return carrito 
            

def mostrar_carrito(carrito):
    print("\nCarrito de compra")
    total_final= 0 

    for item in carrito:
        print(f"{item[0]} - ${item[1]} x {item[2]} = ${item[3]}")
        total_final += item[3]

    print(f"\nTOTAL: ${total_final}")

productos= crear_productos()
mostrar_productos(productos)

carrito=comprar(productos)
mostrar_carrito(carrito)
