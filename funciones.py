import os

def limpiar_pantalla():
    if os.name == "nt":  # Windows
        #Es una funcion de python que ejecuta comandos del sistema operativo.
        os.system("cls")#Le pasamos el comando y lo ejectua en la shell
    else: #Liempia la pantalla Linux y Mac
        os.system("clear")
#---------------------------------------------------------------
#Interfaz de usuario
#---------------------------------------------------------------
def dibujar_borde(titulo, ancho=60):
    print("╔" + "═" * (ancho-2) + "╗")
    print("║" + titulo.center(ancho-2) + "║")
    print("╚" + "═" * (ancho-2) + "╝")
    print()


 ###################VALIDACION DE USUARIOS########################
 
def validar_usuario(empleados,usuario,contra, atributo_empleados):
    for empleado in empleados:
        if empleado[3]==usuario and empleado[5]==contra:
            if empleado[4]=="admin":
                submenu_admin(empleados, atributo_empleados)
            else:
                submenu_empleado()
            return
        print("Inicio de sesion fallido.")
    input("Presione Enter para continuar...")


def login(empleados, atributo_empleados):
    limpiar_pantalla()
    dibujar_borde(" INICIAR SESIÓN ", 40)
    usuario = input("  Usuario: ").strip()
    contra = input("  Contraseña: ").strip()  
    validar_usuario(empleados,usuario,contra, atributo_empleados)

#---------------------------------------------------------------
#REGISTRO USUARIOS
#---------------------------------------------------------------
def registro():
    limpiar_pantalla()
    dibujar_borde(" REGISTRARSE ", 40)
    print("  (Funcionalidad simulada – no guarda nada)")
    input("  Presiona Enter para volver...")

#---------------------------------------------------------------




##---------------------------------------------------------------
#MENU PRINCIPAL 
##---------------------------------------------------------------
def menu_principal(empleados, atributo_empleados):
    while True:
        limpiar_pantalla()
        dibujar_borde(" HAMBURGESAS ", 40)
        print("  1. Iniciar sesión")
        print("  2. Registrarse")
        print("  3. Ver créditos")
        print("  4. Salir")
        print()
        
        opcion = input("  → Elige una opción (1-4): ").strip()

        #opcion de menu
        if opcion == "1":
            login(empleados, atributo_empleados)
        elif opcion == "2":
            registro()
        elif opcion == "3":
            limpiar_pantalla()
            dibujar_borde(" CRÉDITOS ", 40)
            print("  Hecho por Hernan el Crack")
            input("\n  Presiona Enter para volver...")
        elif opcion == "4":
            print("\n  Nos vemos nene, cuidate")
            break
        else:
            print("  Opción inválida... intenta de nuevo")
## --------------------------------------------------------------


#---------------------------------------------------------------
#MENU QUE VISUALIZA EL ADMINISTRADOR 
#---------------------------------------------------------------
def submenu_admin(empleados, atributo_empleados):
    while True:
        limpiar_pantalla()
        print("1.Listar Usuarios ")
        print("2.Crear usuarios")
        print("3.Modificar usuario")
        ##############################################
        #EZE acá esta ventas
        print("4.Ver ventas ")
        print("5.Ver estadisticas")
        print("6.Salir")
        opcion=input("Ingrese el numero de opcion : ")
    
        if opcion=="1":
            print("Listar Usuarios")
            mostrar_empleados(empleados, atributo_empleados)
            input("Presione enter para volver al menu ")
            limpiar_pantalla()
        elif opcion=="2":
            limpiar_pantalla()
            print("Crear usuarios")
            agregar_empleado(empleados)
            input("Presione enter para volver al menu")
            limpiar_pantalla()
        elif opcion=="3":
            print("Modificar usuario")
            modificar_usuario(empleados,atributo_empleados)
            input("Presione enter para volver al menu.")
            limpiar_pantalla()
        elif opcion=="4":
            print("Ver ventas")
        elif opcion=="5":
            print("Ver estadisticas")
        elif opcion=="6":
            print("Salir")
            break
        else:
            print("Opcion no valida")
#---------------------------------------------------------------
#SUBMENU QUE VISUALIZA EL EMPLEADO
#---------------------------------------------------------------
def submenu_empleado():
    while True:
        limpiar_pantalla()
        print("1.Crear venta")
        print("2.Modificar venta")
        print("3.Ver ventas realizadas ")
        print("4.Salir")
        opcion=input("Ingrese el número de opción: ").strip()
        if opcion=="":
            print("La opción no puede encontrarse vacía")
        elif opcion =="1":
            print("Crear venta")
        elif opcion=="2":
            print("Modificar venta")
        elif opcion=="3":
            print("Ver ventas realizadas")      
        elif opcion=="4":
            print("Salir")
            break



#---------------------------------------------------------------  
# Funciones para la gestión de empleados
#---------------------------------------------------------------

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
            rol_user=input("Ingrese el rol del usuario 1-admin o 2-empleado: ").strip()
            if rol_user=="":
                print("El rol no puede estar vacío.")
            elif rol_user not in ["1","2"]:#valida que el rol ingresado sea 1 o 2
                print("Rol no válido. Ingrese 1 para admin o 2 para empleado.")
        if  rol_user=="1":
            rol_user="admin"
        else:
            rol_user="empleado"
        while not contra.isalnum():
            contra=input("Ingrese la contraseña: ").strip()
            if contra=="":
                print("La contraseña no puede estar vacía.")
            elif len(contra) < 6 or len(contra) > 12:#valida rango de caracteres
                print("La contraseña debe tener entre 6 y 12 caracteres.")
            elif not contra.isalnum():#valida que la contraseña solo contenga letras y números
                print("La contraseña no puede contener caracteres especiales.")

        nuevo_id = max(empleado[0] for empleado in empleados) + 1
        empleados.append([nuevo_id,nombre,apellido,user_name,rol_user,contra])#agrega una nueva fila a la matriz de empleados con los datos ingresados
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
                nuevo_rol=input("Ingrese el nuevo rol: ").strip()
                empleado[4]=nuevo_rol
            else:
                print("Opcion invalida")
            return print("Modificado con exito \n",empleado)

    print("Empleado no encontrado")
    


    
            