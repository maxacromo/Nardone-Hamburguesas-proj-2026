import os , re
from .constantes import ID,NOMBRE,APELLIDO,USUARIO,ROL,PASSWORD,ESTADO
from .usuarios import empleados, atributo_empleados
from ventas.menu_ventas import *
from Clientes.Clientes import mostrar_menu_clientes

ancho_menu = 100

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
 
def validar_usuario(empleados, usuario, contra, atributo_empleados):
    for empleado in empleados:

        if empleado[USUARIO]==usuario and empleado[PASSWORD]==contra:
            if empleado[ESTADO]=="Activo" and empleado[ROL]=="admin":
                submenu_admin(empleados, atributo_empleados)
            elif empleado[ESTADO]=="Activo" and empleado[ROL]=="empleado":
                submenu_empleado()
            else:
                print("El usuario ingresado " \
                " se encuentra Inactivo, debe comunicarse con el administrador.")
                input("Presione entender para volver al menu principal")
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
        dibujar_borde("HAMBURGUESERIA", 40)
        print("[1] Iniciar sesión")
        print("[2] Registrarse")
        print("[3] Ver créditos")
        print("[0] Salir")
        print()
        
        opcion = input("→ Elige una opción (1-3): ").strip()

        #opcion de menu
        if opcion == "1":
            login(empleados, atributo_empleados)
        elif opcion == "2":
            registro()
        elif opcion == "3":
            limpiar_pantalla()
            dibujar_borde(" CRÉDITOS ", 40)
            print("Hecho por: Hernan Castro, Gonzales Ezequiel , Zalles Kenaya, Santiago Elcano, Thiago Guarino, Máximo Masi")
            input("Presiona Enter para volver...")
        elif opcion == "0":
            print("Finalizando.")
            break
        else:
            print("Opción inválida... intenta de nuevo")
## --------------------------------------------------------------


#---------------------------------------------------------------
#MENU QUE VISUALIZA EL ADMINISTRADOR 
#---------------------------------------------------------------
def submenu_admin(empleados, atributo_empleados):
    while True:
        limpiar_pantalla()
        print("-"*ancho_menu)
        print("MENÚ PRINCIPAL")
        print("-"*ancho_menu)
        print("[1] Listar Usuarios ")
        print("[2] Crear usuarios")
        print("[3] Modificar usuario")
        print("[4] Módulo de ventas")
        print("[5] Módulo de estadisticas")
        print("[6] Clientes")
        print("[7] Stock")
        print("-"*ancho_menu)
        print("[0] Salir")
        print("-"*ancho_menu)
        print()
        opcion=input("Ingrese el numero de opcion : ")
        limpiar_pantalla()
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
            mostrar_menu_ventas()
        elif opcion=="5":
            mostrar_menu_estadisticas()
        elif opcion=="6":
            mostrar_menu_clientes()
        elif opcion=="0":
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
    entrada_permitida= r'^[A-Za-zÁÉÍÓÚáéíóúÑñ]+(?:[ -][A-Za-zÁÉÍÓÚáéíóúÑñ]+)*$'
    while True:
        data_usuario = input(mensaje).strip()
        
        if data_usuario == "":
            print(f"El {campo} no puede estar vacío.")
        elif not re.fullmatch(entrada_permitida, data_usuario):
            print(f"El {campo} solo puede contener letrasy espacios.")
        else:
            return data_usuario

#---------------------------------------------------------------
#VALIDA QUE EL USUARIO INGRESADO CUMPLA CON LOS REQUISITOS DE LONGITUD Y CARACTERES
#---------------------------------------------------------------
def validacion_usuario(mensaje):
    entrada_permitida= r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{5,8}$'
    while True:
        usuario = input(mensaje).strip()
        if usuario == "":
            print("El nombre de usuario no puede estar vacío.")
        elif not re.fullmatch(entrada_permitida, usuario):
            print("El nombre de usuario debe tener entre 5 y 8 caracteres.")
        else:
            return usuario
        
#---------------------------------------------------------------
#VALIDA QUE LA CONTRASEÑA CUMPLA CON LOS REQUISITOS DE LONGITUD Y CARACTERES
#- --------------------------------------------------------------
def validacion_password(mensaje):
    entrada_permitida= r'^(?=.*[A-Za-z])(?=.*\d).{5,8}$'
    while True:
        password = input(mensaje).strip()
        if password == "":
            print("La contraseña no puede estar vacía.")
        elif not re.fullmatch(entrada_permitida, password):
            print("La contraseña debe tener entre 5 y 10 caracteres y contener al menos una letra y un número.")
        else:
            return password

        
#---------------------------------------------------------------
#VALIDA QUE EL ROL INGRESADO SEA VALIDO
#---------------------------------------------------------------

def validacion_rol(mensaje):
    while True:
        rol=input(mensaje).strip()
        if rol=="":
            print("El rol no puede encontrarse vacio")
        elif rol not in ["1","2"]:#valida que el rol ingresado sea 1 o 2
            print("Rol no válido. Ingrese 1 para admin o 2 para empleado.")
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
        nombre=validacion_letras("Ingrese el nombre del empleado: ","nombre")
        apellido=validacion_letras("Ingrese el apellido del empleado: ","apellido")
        user=validacion_usuario("Ingrese el nombre de usuario: ")
        password=validacion_password("Ingrese la contraseña: ")     
        rol=validacion_rol("Ingrese el rol del usuario 1-admin o 2-empleado: ")
        nuevo_id=obtener_id(empleados)
        estado="Activo"  
        empleados.append([nuevo_id,nombre,apellido,user,rol,password,estado])#agrega una nueva fila a la matriz de empleados con los datos ingresados
        salida=str(input("Para finalizar la carga de usuarios presione X o enter para seguir: ")).lower()
        if salida=="x":
            return 
     
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
#Funcion para pedir ID 
#---------------------------------------------------------------
def solicitar_id(mensaje):
    while True:
        id=input(mensaje).strip()
        if id=="":
            print("El ID no puede encontrarse vacio")
        elif not id.isdigit():
            print("El ID debe ser un número entero.")
        else:
            return id

#---------------------------------------------------------------
# Función para modificar el nombre de usuario de un empleado
#---------------------------------------------------------------

def modificar_usuario(empleados,atributo_empleados):
    mostrar_empleados(empleados,atributo_empleados)
    id_buscado = solicitar_id("Ingrese el ID del empleado a modificar: ")
    for empleado in empleados:
        if empleado[ID] == id_buscado:
            print(empleado)
            print("Ingrese el numero del atributo que desea modificar: ")
            print("1.Nombre")
            print("2.Apellido")
            print("3.Usuario")
            print("4.Rol")
            print("5.Contraseña")
            print("6.Estado del usuario")
            opcion=solicitar_id("Ingrese el numero de la opción: ")
            if opcion=="1":
                nuevo_nombre=validacion_letras("Ingrese el nuevo nombre ", "nombre")
                empleado[NOMBRE]=nuevo_nombre

            elif opcion=="2":
                nuevo_apellido=validacion_letras("Ingrese el nuevo apellido ", "apellido")
                empleado[APELLIDO]=nuevo_apellido
            elif opcion=="3":
                nuevo_usuario=validacion_usuario("Ingrese el nuevo usuario: ")
                empleado[USUARIO]=nuevo_usuario
            elif opcion=="4":
                nuevo_rol=validacion_rol("Ingrese el nuevo  rol asignado ,  1 para admin o 2 para empleado: ")
                empleado[ROL]=nuevo_rol
            elif opcion=="5":
                nueva_pass=validacion_password("Ingrese la nueva contraseña: ")
                empleado[PASSWORD]=nueva_pass
            elif opcion=="6":
                estado_actualizado=modificar_estado(empleados)
                empleado[ESTADO]=estado_actualizado
            else:
                print("Opcion invalida")
            return print("Modificado con exito \n",empleado)

    print("Empleado no encontrado")
#-----------------------------------------------------------
"""
Se toma la decisión de no eliminar ningun usuario dado que generaria una inconsistencia en el sistema.
La idea de poner un "Estado de usuario " es para poder garantizar la seguridad del ingreso, solo si el usuario
se encuentra "activo" podra iniciar sesión 
"""
#-----------------------------------------------------------
    
def modificar_estado(empleados):
    while True:
        nuevo_estado=input("Ingrese el nuevo estado. 1 activo y 2 para Inactivo: ").strip()
        if nuevo_estado not in ["1","2"]:
            print("Opcion no valida, ingrese 1 para activo o 2 para inactivo")
        else:
            return "Activo" if nuevo_estado=="1" else "Inactivo"
        
def mostrar_menu_principal():
    menu_principal(empleados, atributo_empleados)
        