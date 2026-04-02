
def menu_admin(empleados, atributo_empleados):
    while True:
        print("1.Listar Usuarios ")
        print("2.Crear usuarios")
        print("3.Modificar usuario")
        print("4.Ver ventas ")
        print("5.Ver estadisticas")
        print("6.Salir")
        opcion=input("Ingrese el numero de opcion : ")
    
        if opcion=="1":
            print("Listar Usuarios")
            mostrar_empleados(empleados, atributo_empleados)
        elif opcion=="2":
            print("Crear usuarios")
            agregar_empleado(empleados)

        elif opcion=="3":
            print("Modificar usuario")
            modificar_usuario(empleados,atributo_empleados)
        elif opcion=="4":
            print("Ver ventas")
        elif opcion=="5":
            print("Ver estadisticas")
        elif opcion=="6":
            print("Salir")
            break
        else:
            print("Opcion no valida")

        
# Funciones para la gestión de empleados

def agregar_empleado(empleados):
    while True:
        #Reinicia variables en cada alta de empleado
        nombre=""
        apellido=""
        user_name=""
        rol_user=""
        #Validación del nombre
        while not nombre.isalpha():
            nombre=input("Ingrese el nombre del empleado: ").strip()
            if nombre=="":
                print("El nombre no puede estar vacío.")
            elif not  nombre.isalpha():
                print("El nombre no puede contener números o caracteres especiales.")
        #Validación del apellido
        while not apellido.isalpha():
            apellido=input("Ingrese el apellido :").strip()
            if apellido=="":
                print("El apellido no puede estar vacío.")
            elif not apellido.isalpha():
                print("Apellido no puede contener números o caracteres especiales.")
        #Validación del nombre de usuario
        while not user_name.isalpha() :
            user_name=input("Ingrese el usuario: ").strip()
            if user_name=="":
                print("El nombre de usuario no puede estar vacío.")
            elif len(user_name) <4 or len(user_name) > 8:#valida rango de caracteres
                print("El nombre de usuario debe tener entre 4 y 8 caracteres.")
            elif not user_name.isalpha():#valida que el nombre de usuario solo contenga letras
                print("El nombre de usuario no puede contener números o caracteres especiales.")
        #Validación del rol
        while not rol_user.isdigit():
            rol_user=input("Ingrese el rol del usuario 1-admin o 2-user: ").strip()
            if rol_user=="":
                print("El rol no puede estar vacío.")
            elif rol_user not in ["1","2"]:#valida que el rol ingresado sea 1 o 2
                print("Rol no válido. Ingrese 1 para admin o 2 para user.")
        if  rol_user=="1":
            rol_user="admin"
        else:
            rol_user="user"
        nuevo_id = max(empleado[0] for empleado in empleados) + 1
        empleados.append([nuevo_id,nombre,apellido,user_name,rol_user])#agrega una nueva fila a la matriz de empleados con los datos ingresados
        salida=str(input("Para finalizar la carga de usuarios presione X o enter para seguir: ")).lower()
        if salida =="x":
            break
    return empleados
#---------------------------------------------------------------
# Función para mostrar la lista de empleados
#---------------------------------------------------------------
def mostrar_empleados(empleados,atributo_empleados):
    for atributo in atributo_empleados:
        print(f"{atributo:<15}", end=" ")#esto hace que se impriman uno a lado del otro, en controla el final del print.
    print("\n")
    for empleado  in empleados:#recorre cada fila (empleado)
        for dato in empleado:#recorre cada valor dentro de esa fila.
            print(f"{dato:<15}", end=" ")#esto hace que se impriman uno a lado del otro, en controla el final del print.")
        print()

#---------------------------------------------------------------
# Función para modificar el nombre de usuario de un empleado
#---------------------------------------------------------------

def modificar_usuario(empleados,atributo_empleados):
    mostrar_empleados(empleados,atributo_empleados)
    id_buscado = int(input("Ingrese el ID del empleado a modificar: "))
    for empleado in empleados:
        if empleado[0] == id_buscado:
            print(empleado)
            print("Ingrese el numero del atributo que desea modificar: ")
            print("1.Nombre")
            print("2.Apellido")
            print("3.Usuario")
            print("4.Rol")  
            opcion=input("Ingrese el numero de la opción: ")
            if opcion=="1":
                nuevo_nombre=input("Ingrese el nuevo nombre: ").strip()
                empleado[1]=nuevo_nombre
            elif opcion=="2":
                nuevo_apellido=input("Ingrese el nuevo apellido: ").strip()
                empleado[2]=nuevo_apellido
            elif opcion=="3":
                nuevo_usuario=input("Ingrese el nuevo usuario: ").strip()
                empleado[3]=nuevo_usuario
            elif opcion=="4":
                nuevo_rol=input("Ingrese el nuevo rol: ")
                empleado[4]=nuevo_rol
            else:
                print("Opcion invalida")
            return
    print("Empleado no encontrado")
    


    
            