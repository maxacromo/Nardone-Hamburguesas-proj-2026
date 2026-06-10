from Clientes.Clientes_Funciones import *
#from Clientes_Funciones import *
import random,json,pprint
ancho_menu = 100
yesno=["yes","y","no","n"]

def Crear_Cliente(Persona_ID,Cliente,Mail_List,yesno): #Funcion que permite agregar Cliente
    Hold="1"
    Flag=0
    while Flag !=1:
        Aux={}
        Persona=[]
        Flag=0
        try:
            Confirm=input("Quiere agregar un nuevo cliente? y/n:").strip().lower()
            if Confirm.isnumeric()or Confirm not in yesno:
                raise ValueError("Ingreso no valido")

        except ValueError as error:
            print("Error:",error)
            input("Presione enter para volver al menu previo.")
            limpiar_pantalla()
            continue
        if Confirm == "yes" or Confirm == "y":
            Hold=Gen_FullName(Hold,yesno)
            if Hold =="1":
                input("Presione enter para volver al menu previo.")
                limpiar_pantalla()
                pass
            else:
                Pila=Hold.split(" ",1)[0]
                Apellido=Hold.split(" ",1)[1]

                Mail,Cliente_Usuario=Gen_Mail(Mail_List,Pila,Apellido)
                Persona.extend([Hold,Mail,Cliente_Usuario,True])

                Num_list(Persona_ID)
                contador=len(Persona_ID)
                Aux[Persona_ID[contador-1]]=Persona
                Cliente.update(Aux)
                input("Presione enter para volver al menu previo.")
                limpiar_pantalla()

        elif Confirm == "no" or Confirm == "n":
            input("Presione enter para volver al menu previo.")
            limpiar_pantalla()
            Flag=1

            
def Read_Cliente(Cliente): #Permite leer la matriz de clientes

    Title=["ID DE CLIENTE","NOMBRE","CORREO","USUARIO","ACTIVIDAD"]
    aux=0
    while aux != len(Title):
        print(f"{Title[aux]:<25}", end=" ")
        aux+=1
    print()
    for key,value in Cliente.items():
        print(f"{key:<25}", end=" ")
        for i in range(len(value)) :
            print(f"{value[i]:<25}", end=" ")
        print("\n")
    input("Presione enter para volver al menu previo.")
    limpiar_pantalla()


       

def Update_Cliente(Cliente,yesno): #Permite cambiar nombres de usuario pero si a alguien se le ocurre algun valor mas se le puede agregar
    Flag=0
    Choose=[1,2,3,0]
    while Flag == 0:
        print()
        print("1) Modificar Nombre de Cliente")
        print("2) Modificar Apellido de Cliente")
        print("3) Modificar Nombre y Apellido de Cliente")
        print("0) Salir")

        try:
            Check=int(input(":"))
            if Check ==0:
                Flag=1
                input("Presione enter para volver al menu previo.")
                limpiar_pantalla()
                continue
            elif Check not in Choose:
                raise ValueError("Ingreso no valido")
            elif not Check:
                raise ValueError("Elija una opcion")

        except ValueError as error:
            print("Error:",error)
            input("Presione enter para volver al menu previo.")
            limpiar_pantalla()

        
        if Check==1:
            limpiar_pantalla()
            Check,Search,Result=Verificacion_Mod_Usuario(Cliente,yesno,0)
            if Check=="y":
                print("A que quiere cambiar el nombre?")
                Gen_Nombre(Result,yesno)
                Cliente[Search]=Result
            
            elif Check =="n":
                Check="1"
                pass
            else:
                limpiar_pantalla()
                print("Error,ingrese un input valido")
        
        elif Check==2:
            limpiar_pantalla()
            Check,Search,Result=Verificacion_Mod_Usuario(Cliente,yesno,0)
            if Check=="y":
                print("A que quiere cambiar el nombre?")
                Gen_Apellido(Result,yesno)
                Cliente[Search]=Result
            
            elif Check =="n":
                Check="1"
                pass
            else:
                limpiar_pantalla()
                print("Error,ingrese un input valido")
            
        elif Check==3:
            limpiar_pantalla()
            Check,Search,Result=Verificacion_Mod_Usuario(Cliente,yesno,0)
            if Check=="y":
                print("A que quiere cambiar el nombre?")
                Result=Gen_FullName(Result,yesno)
                Cliente[Search][0]=Result
            
            elif Check =="n":
                Check="1"
                pass
            else:
                limpiar_pantalla()
                print("Error,ingrese un input valido")

        elif Check==0:
            Flag=1
            input("Presione enter para volver al menu previo.")
            limpiar_pantalla()

    return Cliente

def Destruir_Cliente(Cliente,yesno):# Permite Borrar clientes
    Flag=0
    Choose=[1,2,0]
    while Flag ==0:
        print("1)Borrar Cliente")
        print("2)Reactivar Cuenta")
        print("0)Salir")

        try:
            Check=int(input(":"))
            if Check ==0:
                Flag=1
                input("Presione enter para volver al menu previo.")
                limpiar_pantalla()
                continue

            elif Check not in Choose:
                raise ValueError("Ingreso no valido")

        except ValueError as error:
            print("Error:",error)
            input("Presione enter para volver al menu previo.")
            limpiar_pantalla()

        if Check==1:
            limpiar_pantalla()
            Check,Search,Result=Verificacion_Mod_Usuario(Cliente,yesno,0)
            if Check == "y":
                Cliente[Search][2]=False
                input("Presione enter para volver al menu previo.")
                limpiar_pantalla()
            
            elif Check =="n":
                Check="1"
                pass
            else:
                input("Presione enter para volver al menu previo.")
                limpiar_pantalla()
                print("Error,ingrese un input valido")

        elif Check==2:
            limpiar_pantalla()
            Check,Search,Result=Verificacion_Mod_Usuario(Cliente,yesno,1)

            if Check == "y":
                Cliente[Search][2]=True
                input("Presione enter para volver al menu previo.")
                limpiar_pantalla()
            
            elif Check =="n":
                Check="1"
                pass
            else:
                limpiar_pantalla()
                print("Error,ingrese un input valido")
        
    
    return Cliente

def Busqueda_Cliente(Cliente,Persona_ID,yesno):
    flag=0
    while flag==0:

        try:
            Search=input("Ingrese el Nombre y apellido del cliente o 0 para salir:")
            if not Search:
                raise ValueError("El Nombre no puede ser vacio")
            elif Search=="0":
                flag=1
                input("Presione enter para volver al menu previo.")
                limpiar_pantalla()
                continue
            elif not Search.replace(" ","").isalpha():
                raise ValueError("Los Nombres no contienen Numeros")

        except ValueError as error:
                print("Error:",error)
                input("Presione enter para volver al menu previo.")
                limpiar_pantalla()    
                continue

        if flag==0:
            Result=Search_Client_Name(Search,Cliente,Persona_ID)
            if Result == "Not Found":
                print("El Cliente",Search,"no se encuentra en la base de datos")
                input("Presione enter para volver al menu previo.")
                limpiar_pantalla()
            else:
                print("El Cliente",Search,"tiene el ID",Result)
                input("Presione enter para volver al menu previo.")
                limpiar_pantalla()


def mostrar_menu_clientes():
    Persona_ID=[]
    Mail_List=[]
    try:
        with open ("Clientes_Datos.json", "r",encoding="UTF-8") as Datos:
            
            Cliente=json.load(Datos)
            Persona_ID=list(Cliente.keys())
            for i in range(len(Persona_ID)):
                Mail_List.append(Cliente[Persona_ID[i]][1])
    except(FileNotFoundError,OSError) as error:
        print("Error:",error)
    finally:
        Datos.close


    limpiar_pantalla()
    while True:
        Check=-1
        print("-"*ancho_menu)
        print("MENÚ PRINCIPAL > MENÚ DE CLIENTES")
        print("-"*ancho_menu)
        print("Seleccione una opcion:")
        print("[1] Crear Cliente")
        print("[2] Leer Cliente")
        print("[3] Modificar Cliente")
        print("[4] Borrar Cliente")
        print("[5] Buscar Cliente")
        print("-"*ancho_menu)
        print("[0] Salir")
        print("-"*ancho_menu)
        Choose=[1,2,3,4,5,0]
        try:
            Check=int(input(":"))
            if Check not in Choose:
                raise ValueError("Ingreso no valido")

        except ValueError as error:
            print("Error:",error)
            input("Presione enter para volver al menu previo.")
            limpiar_pantalla()
        if Check==1:
            limpiar_pantalla()
            Crear_Cliente(Persona_ID,Cliente,Mail_List,yesno)
            #Update_Client_File(Cliente)


        elif Check ==2:
            limpiar_pantalla()
            Read_Cliente(Cliente)
            #pprint.pprint(Cliente)


        elif Check==3:
            limpiar_pantalla()
            Update_Cliente(Cliente,yesno)
            #Update_Client_File(Cliente)

        elif Check==4:
            limpiar_pantalla()
            Destruir_Cliente(Cliente,yesno)
            #Update_Client_File(Cliente)

        elif Check==5:
            limpiar_pantalla()
            Busqueda_Cliente(Cliente,Persona_ID,yesno)
            #Update_Client_File(Cliente)

        elif Check==0:
            print("Bye!")
            Cleanup(Cliente,Persona_ID)
            Update_Client_File(Cliente)
            break
        else :
            limpiar_pantalla()
            print("Error,ingrese un input valido")


def buscar_cliente_by_user(user):
    try:
        with open("Clientes_Datos.json", "r", encoding="UTF-8") as Datos:
            Clientes_list = json.load(Datos)
            for cliente in Clientes_list:
                if user == Clientes_list[cliente][2]:
                    return cliente
            raise ValueError(f"Cliente '{user}' no encontrado")

    except (FileNotFoundError, OSError) as error:
        print("Error:", error)
    finally:
        Datos.close()


def buscar_o_crear_cliente(Persona_ID, Cliente, Mail_List, yesno):
    try:
        usuario_cliente = input("Ingrese el Usuario del cliente: ").strip()
        resultado = buscar_cliente_by_user(usuario_cliente)
        print(f"Cliente encontrado: {resultado}")
        return resultado

    except ValueError:
        print(f"El usuario '{usuario_cliente}' no existe. Creando cliente...")
        Hold = "1"
        while Hold == "1":
            Hold = Gen_FullName("1", yesno)

        Pila = Hold.split(" ", 1)[0]
        Apellido = Hold.split(" ", 1)[1]
        Mail, Cliente_Usuario = Gen_Mail(Mail_List, Pila, Apellido)
        Persona = [Hold, Mail, Cliente_Usuario, True]
        Num_list(Persona_ID)
        contador = len(Persona_ID)
        Aux = {Persona_ID[contador - 1]: Persona}
        Cliente.update(Aux)
        print("Cliente creado exitosamente.")
        return Persona_ID[contador - 1]

    except (FileNotFoundError, OSError) as error:
        print("Error al leer el archivo:", error)
        return None

def cargar_clientes():
    Persona_ID = []
    Mail_List = []
    Cliente = {}
    try:
        with open("Clientes_Datos.json", "r", encoding="UTF-8") as Datos:
            Cliente = json.load(Datos)
            Persona_ID = list(Cliente.keys())
            for i in range(len(Persona_ID)):
                Mail_List.append(Cliente[Persona_ID[i]][1])
    except (FileNotFoundError, OSError) as error:
        print("Error:", error)
    return Persona_ID, Cliente, Mail_List
