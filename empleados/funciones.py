import os
from empleados.constantes import ID,NOMBRE,APELLIDO,USUARIO, ROL,PASSWORD,ESTADO
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

        if empleado[USUARIO]==usuario and empleado[PASSWORD]==contra:
            if empleado[ESTADO]=="Activo" and empleado[ROL]=="admin":
                submenu_admin(empleados, atributo_empleados)
            elif empleado[ESTADO]=="Activo" and empleado[ROL]=="empleado":
                submenu_empleado()
            else:
                print("El usuario ingresado " \
                " se encuentra Inactivo, debe comunicarse con el admisnitrador.")
                input("Presione entender para volver al menu principal")
            return
        print("Inicio de sesion fallido.")
    input("Presione Enter para continuar...")


def login(empleados, atributo_empleados):
    limpiar_pantalla()
    dibujar_borde(" INICIAR SESIÓN ", 40)
    usuario = input("  \033[1;37mUsuario: \033[0m").strip()
    contra = input("  \033[1;37mContraseña: \033[0m").strip()  
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
        dibujar_borde(" \033[1;33m🍔 HAMBURGESAS 🍔\033[0m", 40)
        print("  \033[1;34m1. Iniciar sesión\033[0m")
        print("  \033[1;34m2. Registrarse\033[0m")
        print("  \033[1;34m3. Ver créditos\033[0m")
        print("  \033[1;34m4. Salir\033[0m")
        print()
        
        opcion = input("\033[1;37m  → Elige una opción (1-4): \033[0m")

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
            print("  \033[1;31mOpción inválida... intenta de nuevo\033[0m")
## --------------------------------------------------------------


#---------------------------------------------------------------
#MENU QUE VISUALIZA EL ADMINISTRADOR 
#---------------------------------------------------------------

    
def submenu_admin(empleados, atributo_empleados):
    while True:
        limpiar_pantalla()
        print("  \033[1;34m1. Listar Usuarios\033[0m")
        print("  \033[1;34m2. Crear usuarios\033[0m")
        print("  \033[1;34m3. Modificar usuario\033[0m")
        ##############################################
        #EZE acá esta ventas
        print("  \033[1;34m4. Módulo de ventas\033[0m")
        print("  \033[1;34m5. Ver estadisticas\033[0m")
        print("  \033[1;34m6. Salir\033[0m")
        opcion=input("\033[1;37mIngrese el numero de opcion : \033[0m")
        limpiar_pantalla()
        if opcion=="1":
            print(" \033[1;34mListar Usuarios\033[0")
            mostrar_empleados(empleados, atributo_empleados)
            input("\n\033[1;34mPresione Enter para volver al menu...\033[0m")
            limpiar_pantalla()
        elif opcion=="2":
            limpiar_pantalla()
            print("Crear usuarios")
            agregar_empleado(empleados)
            input("\033[1;34mPresione Enter para volver al menu...\033[0m")
            limpiar_pantalla()
        elif opcion=="3":
            print("Modificar usuario")
            modificar_usuario(empleados,atributo_empleados)
            input("\033[1;34mPresione enter para volver al menu.\033[0m")
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
def validacion_letras(mensaje, campo):
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("\033[1;34m"+f"El {campo} no puede estar vacío.\033[0m")
        elif not valor.isalpha():
            print("\033[1;31m"+f"El {campo} no puede contener números o caracteres especiales.\033[0m")
        else:
            return valor

#---------------------------------------------------------------
#VALIDA QUE EL USUARIO INGRESADO CUMPLA CON LOS REQUISITOS DE LONGITUD Y CARACTERES
#---------------------------------------------------------------
def validacion_usuario(mensaje):
    while True:
        usuario=input(mensaje).strip()
        if usuario=="":
            print("\033[1;31mEl nombre de usuario no puede estar vacio.\033[0m")
        elif len(usuario)<5 or len(usuario)>8:
            print("\033[1;33mEl nombre de usuario debe tener entre 5 y 8 caracteres.\033[0m")
        elif not usuario.isalnum():
            print("\033[1;31mEl nombre de usuario no puede contener caracteres especiales.\033[0m")
        elif usuario.isnumeric():
            print("\033[1;31mEl nombre de usuario no puede contener solo números.\033[0m")
        elif usuario.isalpha():
            print("\033[1;31mEl nombre de usuario no puede contener solo letras.\033[0m")
        else:
            return usuario
        
#---------------------------------------------------------------
#VALIDA QUE LA CONTRASEÑA CUMPLA CON LOS REQUISITOS DE LONGITUD Y CARACTERES
#- --------------------------------------------------------------
def validacion_password(mensaje):
    while True:
        password=input(mensaje).strip()
        if password =="":
            print("\033[1;31mLa contraseña no puede estar vacia\033[0m")
        elif len(password)<5 or len(password) >10:
            print("\033[1;33mLa contraseña debe contener entre 5 y 10 caracteres\033[0m")
        elif password.isalpha():
            print("\033[1;33mLa contraseña no puede tener solo letras\033[0m")
        elif password.isnumeric():
            print("\033[1;33mLa contraseña no puede contener solo numeros\033[0m")
        else:
            return password
        
#---------------------------------------------------------------
#VALIDA QUE EL ROL INGRESADO SEA VALIDO
#---------------------------------------------------------------

def validacion_rol(mensaje):
    while True:
        rol=input(mensaje).strip()
        if rol=="":
            print("\033[1;31mEl rol no puede encontrarse vacio\033[0m")
        elif rol not in ["1","2"]:#valida que el rol ingresado sea 1 o 2
            print("\033[1;31mRol no válido. Ingrese 1 para admin o 2 para empleado.\033[0m")
        else:
            return "admin" if rol=="1" else "empleado"

#---------------------------------------------------------------
#Funcion para obtener el nuevo ID para un empleado, sumando 1 al ID mas alto existente en la lista de empleados.
#----------------------------------------------------------------
def obtener_id(empleados):
    nuevo_id = max(empleado[ID] for empleado in empleados) + 1
    return nuevo_id
#----------------------------------------------------------------
#VALIDACION DE ESTADO DEL USUARIO
#----------------------------------------------------------------





#----------------------------------------------------------------
#Llamo todas las funciones para generar al nuevo empleado. 
#---------------------------------------------------------------
def agregar_empleado(empleados):
    while True:
        nombre=validacion_letras("\033[1;37mIngrese el nombre del empleado: \033[0m", "nombre")
        apellido=validacion_letras("\033[1;37mIngrese el apellido del empleado: \033[0m", "apellido")
        user=validacion_usuario("\033[1;37mIngrese el nombre de usuario: \033[0m")
        password=validacion_password("\033[1;37mIngrese la contraseña: \033[0m")     
        rol=validacion_rol("\033[1;37mIngrese el rol del usuario 1-admin o 2-empleado: \033[0m")
        nuevo_id=obtener_id(empleados)
        estado="Activo"  
        empleados.append([nuevo_id,nombre,apellido,user,rol,password,estado])#agrega una nueva fila a la matriz de empleados con los datos ingresados
        salida=str(input("\033[1;34mPara finalizar la carga de usuarios presione X o enter para seguir: \033[0m")).lower()
        if salida=="x":
            return 
     
#---------------------------------------------------------------
# Función para mostrar la lista de empleados
#---------------------------------------------------------------
def mostrar_empleados(empleados,atributo_empleados):
    for atributo in atributo_empleados:
        print("\033[1;33m"f"{atributo:<15}\033[0m", end=" ")#esto hace que se impriman uno a lado del otro, en controla el final del print.
         
    print("\n")
    #print("\033[32m" + "─" * 112 + "\033[0m") 
    for empleado  in empleados:#recorre cada fila (empleado)
        print("\033[1;35m" + "─" * 105 + "\033[0m")
        for dato in empleado:#recorre cada valor dentro de esa fila.
            print("\033[1;37m"f"{dato:<15}\033[0m", end=" ")#esto hace que se impriman uno a lado del otro, en controla el final del print.")
        print()
        print("\033[1;35m" + "─" * 105 + "\033[0m")

#---------------------------------------------------------------
# Función para modificar el nombre de usuario de un empleado
#---------------------------------------------------------------
def modificar_usuario(empleados,atributo_empleados):
    mostrar_empleados(empleados,atributo_empleados)
    id_buscado = int(input("\033[1;34mIngrese el ID del empleado a modificar: \033[0m"))
    for empleado in empleados:
        if empleado[ID] == id_buscado:
            print(empleado)
            print(" \033[1;33mIngrese el numero del atributo que desea modificar: \033")
            print(" \033[1;34m1.Nombre\033[0m")
            print(" \033[1;34m2.Apellido\033[0m")
            print(" \033[1;34m3.Usuario\033[0m")
            print(" \033[1;34m4.Rol\033[0m")
            print(" \033[1;34m5.Contraseña\033[0m")
            print(" \033[1;34m6.Estado del usuario\033[0m")
            opcion=input("\033[1;33mIngrese el numero de la opción: \033[0m")
            if opcion=="1":
                nuevo_nombre=validacion_letras("\033[1;34mIngrese el nuevo nombre: \033[0m", "nombre")
                empleado[NOMBRE]=nuevo_nombre

            elif opcion=="2":
                nuevo_apellido=validacion_letras("\033[1;34mIngrese el nuevo apellido: \033[0m", "apellido")
                empleado[APELLIDO]=nuevo_apellido
            elif opcion=="3":
                nuevo_usuario=validacion_usuario("\033[1;34mIngrese el nuevo usuario: \033[0m")
                empleado[USUARIO]=nuevo_usuario
            elif opcion=="4":
                nuevo_rol=validacion_rol("\033[1;34mIngrese el nuevo rol asignado ,  1 para admin o 2 para empleado: \033[0m")
                empleado[ROL]=nuevo_rol
            elif opcion=="5":
                nueva_pass=validacion_password("\033[1;34mIngrese la nueva contraseña: \033[0m")
                empleado[PASSWORD]=nueva_pass
            elif opcion=="6":
                estado_actualizado=modificar_estado(empleados)
                empleado[ESTADO]=estado_actualizado
            else:
                print("\033[1;31mOpcion invalida\033[0m")
            return print("\033[1;32mModificado con exito \n\033[0m",empleado)

    print("\033[1;31mEmpleado no encontrado\033[0m")
#-----------------------------------------------------------
"""
Se toma la decisión de no eliminar ningun usuario dado que generaria una inconsistencia en el sistema.
La idea de poner un "Estado de usuario " es para poder garantizar la seguridad del ingreso, solo si el usuario
se encuentra "activo" podra iniciar sesión 
"""
#-----------------------------------------------------------
    
def modificar_estado(empleados):
    while True:
        nuevo_estado=input("\033[1;37mIngrese el nuevo estado. 1 activo y 2 para Inactivo: \033[0m").strip()
        if nuevo_estado not in ["1","2"]:
            print("\033[1;31mOpcion no valida, ingrese 1 para activo o 2 para inactivo\033[0m")
        else:
            return "\033[1;32mActivo\033[0m" if nuevo_estado=="1" else "\033[1;31mInactivo\033[0m"