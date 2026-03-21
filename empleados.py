git def agregar_empleado():
    empleados=[]
    id_empleado=0
    while True:
        while True:
            nombre=input("Ingrese el nombre del empleado: ").strip()
            if nombre=="":
                print("El nombre no puede estar vacío.")
            elif nombre.isalpha():
                break
            else:
                print("Nombre no puede contener números o caracteres especiales.")
        while True:
            apellido=input("Ingrese el apellido :").strip()
            if apellido=="":
                print("El apellido no puede estar vacío.")
            elif apellido.isalpha():
                break
            else:
                print("Apellido no puede contener números o caracteres especiales.")
        while True:
            user_name=input("Ingrese el usuario: ").strip()
            if user_name=="":
                print("El nombre de usuario no puede estar vacío.")
            elif len(user_name) <4 or len(user_name) > 8:#valida rango de caracteres
                print("El nombre de usuario debe tener entre 4 y 8 caracteres.")
            elif user_name.isalpha():#valida que el nombre de usuario solo contenga letras
                break
            else:
                print("El nombre de usuario no puede contener números o caracteres especiales.")
        while True:
            rol_user=input("Ingrese el rol del usuario 1-admin o 2-user: ").strip()
            if rol_user=="":
                print("El rol no puede estar vacío.")
            elif rol_user not in ["1","2"]:#valida que el rol ingresado sea 1 o 2
                print("Rol no válido. Ingrese 1 para admin o 2 para user.")
            elif rol_user=="1":
                rol_user="admin"
                break
            elif rol_user=="2":
                rol_user="user"
                break
        id_empleado+=1
        empleados.append([id_empleado,nombre,apellido,user_name,rol_user])#agrega una nueva fila a la matriz de empleados con los datos ingresados
        salida=str(input("Para finalizar la carga de usuarios presione X o enter para seguir: ")).lower()
        if salida =="x":
            break
    return empleados
def mostrar_empleados(empleados,atributo_empleados):
    for atributo in atributo_empleados:
        print(f"{atributo:<15}", end=" ")#esto hace que se impriman uno a lado del otro, en controla el final del print.
    print("\n")
    for empleado  in empleados:#recorre cada fila (empleado)
        for dato in empleado:#recorre cada valor dentro de esa fila.
            print(f"{dato:<15}", end=" ")#esto hace que se impriman uno a lado del otro, en controla el final del print.")
        print()
def modificar_usuario(empleados):
    id_buscado = int(input("Ingrese el ID del empleado a modificar: "))

    for empleado in empleados:
        if empleado[0] == id_buscado:
            while True:
                nuevo_user = input("Ingrese nuevo usuario: ").strip()

                if nuevo_user == "":
                    print("El nombre de usuario no puede estar vacío.")
                elif len(nuevo_user) < 4 or len(nuevo_user) > 8:
                    print("El nombre de usuario debe tener entre 4 y 8 caracteres.")
                elif not nuevo_user.isalpha():
                    print("El nombre de usuario solo puede contener letras y números.")
                else:
                    empleado[3] = nuevo_user
                    print("Usuario modificado exitosamente.")
                    return
atributo_empleados=["Id_empleado","Nombre","Apellido","usuario","Rol"]
matriz_empleados=agregar_empleado()
mostrar_empleados(matriz_empleados,atributo_empleados)#Ya me muestra la matriz por el for que tiene la funcion.
modificar_usuario(matriz_empleados)
mostrar_empleados(matriz_empleados,atributo_empleados)

                                           