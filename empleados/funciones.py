import os , re 
from .constantes import ID_EMPLEADO,NOMBRE,APELLIDO,USUARIO,ROL,PASSWORD,ESTADO
from .usuarios import empleados, atributo_empleados
from ventas.menu_ventas import *
from Clientes.Clientes import mostrar_menu_clientes
from stock.Main_stock import menu
from .colores import *
from productos.menu_productos import menu_productos

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

def buscar_usuario_secuencial(empleados, usuario, contra):
    """
    Aplica el algoritmo búsqueda secuencial.
    Recorre la lista elemento por elemento usando un índice y una bandera.
    """
    i = 0
    encontrado = False
    empleado_encontrado = None
    
    while i < len(empleados) and not encontrado:
        if empleados[i][USUARIO] == usuario and empleados[i][PASSWORD] == contra:
            encontrado = True
            empleado_encontrado = empleados[i]
        else:
            i += 1
            
    return empleado_encontrado
 
def validar_usuario(empleados, usuario, contra, atributo_empleados):
    #Aplicamos el método de búsqueda secuencial
    empleado = buscar_usuario_secuencial(empleados, usuario, contra)
    
    #Evaluamos el resultado de la búsqueda
    if empleado is not None:
        if empleado[ESTADO] != "Activo":
            print("El usuario ingresado se encuentra inactivo, debe comunicarse con el administrador.")
            input("Presione Enter para volver al menú principal")
            return "INACTIVO"
            
        if empleado[ROL] == "admin":
            submenu_admin(empleados, atributo_empleados, usuario)
        elif empleado[ROL] == "empleado":
            submenu_empleado(usuario)
        else:
            print("Rol no verificado.")
            input("Presione Enter para volver al menú principal")
            return False
            
        return True

    return False

def login(empleados, atributo_empleados):
    sesion = 0

    while sesion < 3:
        limpiar_pantalla()
        dibujar_borde(" INICIAR SESIÓN ", 40)
        usuario = input("  Usuario: ").strip()
        contra = input("  Contraseña: ").strip()

        resultado_validacion = validar_usuario(empleados, usuario, contra, atributo_empleados)
        if resultado_validacion == "INACTIVO":
            return
        elif resultado_validacion == True:
            return

        sesion += 1
        print("Usuario o contraseña incorrectos.")
        print(f"Quedan {3 - sesion} intentos.")
        input("Presione Enter para continuar...")
    print("Has excedido el número de intentos. Volviendo al menú principal.")
    input("Presione Enter para continuar...")

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
        
        try:
            opcion = int(input("→ Elige una opción (1-3): ").strip())

            #opcion de menu
            if opcion == 1:
                login(empleados, atributo_empleados)
            elif opcion == 2:
                registro()
            elif opcion == 3:
                limpiar_pantalla()
                dibujar_borde(" CRÉDITOS ", 40)
                print("Hecho por:  Gonzales Ezequiel , Zalles Kenaya, Santiago Elcano, Thiago Guarino, Máximo Masi")
                input("Presiona Enter para volver...")
            elif opcion == 0:
                print("Finalizando.")
                break
            else:
                print("Opción inválida... intenta de nuevo")
                input("Presione Enter para continuar...")
        except ValueError:
            print("Error: Ingrese un número válido.")
            input("Presione Enter para continuar...")
## --------------------------------------------------------------


#---------------------------------------------------------------
#MENU QUE VISUALIZA EL ADMINISTRADOR 
#---------------------------------------------------------------
def submenu_admin(empleados, atributo_empleados, usuario_sesion):
    while True:
        limpiar_pantalla()
        print("-"*ancho_menu)
        print("MENÚ PRINCIPAL")
        print("-"*ancho_menu)
        print("[1] Listar Usuarios ")
        print("[2] Crear usuarios")
        print("[3] Modificar usuario")
        print("[4] Módulo de Ventas")
        print("[5] Módulo de Estadisticas")
        print("[6] Módulo de Clientes")
        print("[7] Administracion de Stock")
        print("[8] Administracion de Productos")
        print("-"*ancho_menu)
        print("[0] Salir")
        print("-"*ancho_menu)
        print()

        try:
            opcion=int(input("Ingrese el numero de opcion : "))
            limpiar_pantalla()
            if opcion==1:
                print(f"{FONDO_CELESTE}{BLANCO} Listar Usuarios {RESET}")
                mostrar_empleados(empleados, atributo_empleados)
                input("Presione enter para volver al menu ")
                limpiar_pantalla()
            elif opcion==2:
                limpiar_pantalla()
                print(f"{FONDO_CELESTE}{BLANCO} Crear usuarios {RESET}")
                agregar_empleado(empleados)
                input("Presione enter para volver al menu")
                limpiar_pantalla()
            elif opcion==3:
                print(f"{FONDO_CELESTE}{BLANCO} Modificar usuario {RESET}")
                modificar_usuario(empleados,atributo_empleados)
                input("Presione enter para volver al menu.")
                limpiar_pantalla()
            elif opcion==4:
                mostrar_menu_ventas(usuario_sesion)
            elif opcion==5:
                mostrar_menu_estadisticas()
            elif opcion==6:
                mostrar_menu_clientes()
            elif opcion == 7:
                menu()
            elif opcion == 8:
                menu_productos()
            elif opcion==0:
                print("Salir")
                break
            else:
                print("Opcion no valida")
        except ValueError:
            print("Error: Ingrese un número válido.")
            input("Presione Enter para continuar...")
            limpiar_pantalla()
#---------------------------------------------------------------
#SUBMENU QUE VISUALIZA EL EMPLEADO
#---------------------------------------------------------------
def submenu_empleado(usuario_sesion):
    while True:
        limpiar_pantalla()
        print("-"*ancho_menu)
        print("MENÚ PRINCIPAL")
        print("-"*ancho_menu)
        print("[1] Crear venta")
        print("[2] Módulo de Estadisticas")
        print("[3] Visualizar ventas")
        print("-"*ancho_menu)
        print("[0] Salir")
        print("-"*ancho_menu)

        try:
            opcion=int(input("Ingrese el número de opción: ").strip())
            if opcion ==1:
                mostrar_creacion_ventas_menu(usuario_sesion)
            elif opcion==2:
                mostrar_menu_estadisticas()
            elif opcion==3:
                mostrar_ventas_menu()    
            elif opcion==0:
                print("Salir")
                break
        except ValueError:
            print("Error: Ingrese un número válido.")
            input("Presione Enter para continuar...")
            limpiar_pantalla()



#---------------------------------------------------------------  
# Funciones para la gestión de empleados
#---------------------------------------------------------------
def validacion_letras(mensaje, campo):
    entrada_permitida= r'^[A-Za-zÁÉÍÓÚáéíóúÑñ]+(?:[ -][A-Za-zÁÉÍÓÚáéíóúÑñ]+)*$'
    data_usuario = input(mensaje).strip()
    while data_usuario == "":
            
        print(f"El {campo} no puede estar vacío.")
        data_usuario = input(mensaje).strip()
        
    while not re.match(entrada_permitida, data_usuario):
        print(f"El {campo} solo puede contener letras y espacios.")
        data_usuario = input(mensaje).strip()
    
    return data_usuario

#---------------------------------------------------------------
#VALIDA QUE EL USUARIO INGRESADO CUMPLA CON LOS REQUISITOS DE LONGITUD Y CARACTERES
#---------------------------------------------------------------
def validacion_usuario(mensaje):
    entrada_permitida= r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{5,8}$'

    usuario = input(mensaje).strip()
        
    while usuario == "":
        print("El nombre de usuario no puede estar vacío.")
        usuario = input(mensaje).strip()
                
    while not re.match(entrada_permitida, usuario):
        print("El nombre de usuario debe contener letras y números.")
        usuario = input(mensaje).strip() 
    return usuario
        
#---------------------------------------------------------------
#VALIDA QUE LA CONTRASEÑA CUMPLA CON LOS REQUISITOS DE LONGITUD Y CARACTERES
#- --------------------------------------------------------------
def validacion_password(mensaje):
    entrada_permitida= r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{5,8}$'
    password = input(mensaje).strip()
    while password == "" or not re.match(entrada_permitida, password):
        print("La contraseña no puede estar vacía.")
        print("Y debe tener entre 5 y 8 caracteres con al menos un número.")
        password = input(mensaje).strip()
    return password
    

        
#---------------------------------------------------------------
#VALIDA QUE EL ROL INGRESADO SEA VALIDO
#---------------------------------------------------------------

def validacion_rol(mensaje):
    bandera_estado=False
    rol_asignado = ""
    while not bandera_estado:
        try:
            rol = int(input(mensaje).strip())
            if rol == 1:
                rol_asignado = "admin"
                bandera_estado=True
            elif rol == 2:
                rol_asignado = "empleado"
                bandera_estado=True
            else:
                print("Rol no válido. Ingrese 1 para admin o 2 para empleado.")
        except ValueError:
            print("Error: Ingrese un número válido (1 o 2).")
    return rol_asignado

#---------------------------------------------------------------
#Funcion para obtener el nuevo ID para un empleado, sumando 1 al ID mas alto existente en la lista de empleados.
#----------------------------------------------------------------
def obtener_id(empleados):
    nuevo_id = max(empleado[ID_EMPLEADO] for empleado in empleados) + 1
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
        empleados.append({
            ID_EMPLEADO: nuevo_id,
            NOMBRE: nombre,
            APELLIDO: apellido,
            USUARIO: user,
            ROL: rol,
            PASSWORD: password,
            ESTADO: estado
        })#agrega un nuevo diccionario a la lista de empleados con los datos ingresados
        salida=str(input("Para finalizar la carga de usuarios presione X o enter para seguir: ")).lower()
        if salida=="x":
            return 
     
#---------------------------------------------------------------
# Función para mostrar la lista de empleados
#---------------------------------------------------------------
def mostrar_empleados(empleados,atributo_empleados):
    # Imprimir encabezados en color CYAN
    for atributo in atributo_empleados:
        print(f"{CYAN}{NEGRITA}{atributo:<15}{RESET}", end=" ")
    print()
    print("-" * 105) # Linea divisoria del encabezado
    
    for empleado in empleados:
        for i, dato in enumerate(empleado.values()):
            # Aplicamos colores dependiendo del texto
            if i == 0:
                print(f"{ROSA}{str(dato):<15}{RESET}", end=" ")
            elif str(dato) == "Inactivo":
                print(f"{ROJO}{str(dato):<15}{RESET}", end=" ")
            elif str(dato) == "Activo":
                print(f"{VERDE}{str(dato):<15}{RESET}", end=" ")
            elif str(dato) == "admin":
                print(f"{NARANJA}{str(dato):<15}{RESET}", end=" ")
            elif str(dato) == "empleado":
                print(f"{AZUL}{str(dato):<15}{RESET}", end=" ")
            else:
                print(f"{str(dato):<15}", end=" ")
        print()
        print("-" * 105) # Linea divisoria entre empleados
#---------------------------------------------------------------
#Funcion para pedir ID 
#---------------------------------------------------------------
def solicitar_id(mensaje):
    id_valido = False #Nuestra bandera empieza en Falso
    id_numero = 0 #Preparamos la variable donde guardaremos el resultado
    
    while not id_valido:
        id_texto = input(mensaje).strip()
        
        if id_texto == "":
            print("El ID no puede encontrarse vacio.")
        else:
            try:
                #Convertimos el texto en número
                id_numero = int(id_texto)
                #Si la conversión fue exitosa, cambiamos la bandera para salir del bucle
                id_valido = True
            except ValueError:
                #Si el usuario ingresó letras, int() falla y salta aquí
                print("El ID debe ser un número entero válido (no se permiten letras).")
                
    # Una vez que el bucle termina, devolvemos el número
    return id_numero

#---------------------------------------------------------------
# Función para modificar el nombre de usuario de un empleado
#---------------------------------------------------------------

def modificar_usuario(empleados,atributo_empleados):
    mostrar_empleados(empleados,atributo_empleados)
    id_buscado = solicitar_id("Ingrese el ID del empleado a modificar: ")
    for empleado in empleados:
        if empleado[ID_EMPLEADO] == id_buscado:
            print(empleado)
            print(f"{FONDO_CELESTE}{BLANCO} Ingrese el numero del atributo que desea modificar: {RESET}")
            print("1.Nombre")
            print("2.Apellido")
            print("3.Usuario")
            print("4.Rol")
            print("5.Contraseña")
            print("6.Estado del usuario")

            try:

                opcion=int(input("Ingrese el numero de la opción: "))
                if opcion==1:
                    nuevo_nombre=validacion_letras("Ingrese el nuevo nombre ", "nombre")
                    empleado[NOMBRE]=nuevo_nombre

                elif opcion==2:
                    nuevo_apellido=validacion_letras("Ingrese el nuevo apellido ", "apellido")
                    empleado[APELLIDO]=nuevo_apellido
                elif opcion==3:
                    nuevo_usuario=validacion_usuario("Ingrese el nuevo usuario: ")
                    empleado[USUARIO]=nuevo_usuario
                elif opcion==4:
                    nuevo_rol=validacion_rol("Ingrese el nuevo  rol asignado ,  1 para admin o 2 para empleado: ")
                    empleado[ROL]=nuevo_rol
                elif opcion==5:
                    nueva_pass=validacion_password("Ingrese la nueva contraseña: ")
                    empleado[PASSWORD]=nueva_pass
                elif opcion==6:
                    estado_actualizado=modificar_estado(empleados)
                    empleado[ESTADO]=estado_actualizado
                else:
                    print("Opcion invalida")
                return print("Modificado con exito \n",empleado)
            except ValueError:
                print("Error: Ingrese un número válido.")
                input("Presione Enter para continuar...")
                limpiar_pantalla()

    print("Empleado no encontrado")
#-----------------------------------------------------------
"""
Se toma la decisión de no eliminar ningun usuario dado que generaria una inconsistencia en el sistema.
La idea de poner un "Estado de usuario " es para poder garantizar la seguridad del ingreso, solo si el usuario
se encuentra "activo" podra iniciar sesión 
"""
#-----------------------------------------------------------
    
def modificar_estado(empleados):
    estado_valido = False
    estado_final = ""
    while not estado_valido:
        try:
            nuevo_estado = int(input(f"Ingrese el nuevo estado. 1 {VERDE}activo{RESET} y 2 para {ROJO}Inactivo{RESET}: ").strip())
            if nuevo_estado == 1:
                estado_final = "Activo"
                estado_valido = True
            elif nuevo_estado == 2:
                estado_final = "Inactivo"
                estado_valido = True
            else:
                print("Opcion no valida, ingrese 1 para activo o 2 para inactivo")
        except ValueError:
            print("Error: Ingrese un número válido (1 o 2).")
    return estado_final
        
def mostrar_menu_principal():
    menu_principal(empleados, atributo_empleados)



        