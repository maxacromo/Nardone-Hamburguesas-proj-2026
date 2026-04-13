def crear_productos():
    productos = []

    n = int(input("¿Cuántos productos querés cargar?: "))

    for i in range(n):
        print(f"\nProducto {i+1}")

    
        codigo = i + 1

        
        while True:
            descripcion = input("Descripción: ")
            if descripcion.strip() != "":
                break
            print("Error: la descripción no puede estar vacía")

        
        while True:
            try:
                precio = int(input("Precio: "))
                if precio > 0:
                    break
                else:
                    print("Error: el precio debe ser mayor a 0")
            except:
                print("Error: ingresá un número válido")

      
        producto = [codigo, descripcion, precio]
        productos.append(producto)

    return productos


def mostrar_productos(productos):
    print("\nLista de productos:")
    print("-" * 40)
    print(f"{'COD':<5}{'DESCRIPCIÓN':<25}{'PRECIO':>10}")
    print("-" * 40)

    for p in productos:
        print(f"{p[0]:<5}{p[1]:<25}${p[2]:>9}")

    print("-" * 40)

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



def eliminar_producto(productos):
    codigo = int(input("Ingrese código de producto a eliminar: "))

    for i in range(len(productos)):
        if productos[i][0] == codigo:
            productos.pop(i)
            print("Producto eliminado")
            return
    
    print("Producto no encontrado")



productos= crear_productos()
mostrar_productos(productos)
#eliminar_producto(productos)
#mostrar_productos(productos)

carrito=comprar(productos)
mostrar_carrito(carrito)


