from Clientes_Funciones import *
import random, pprint

def Persona_Relleno(): #Genera Personas no reales para que el sistema cargue con Cliente ya existen
    Persona_ID=[]
    Mail_List=[]
    Cliente={}
    cycle=random.randint(5,10)
    cont=0
    while cont != cycle:
        Persona=Creador_Personas(Mail_List) 

        def Creador_Usuarios():
            Num_list(Persona_ID)
            Cliente[Persona_ID[cont]]=Persona
            return Cliente
        Creador_Usuarios()
        cont+=1

    return Cliente, Persona_ID, Mail_List


def Crear_Cliente(Persona_ID,Cliente,Mail_List): #Funcion que permite agregar Cliente
    Hold=""
    Flag=0
    while Flag !=1:
        Aux={}
        Persona=[]
        Flag=0
        Confirm=input("Quiere agregar un nuevo cliente? y/n:").strip()
        if Confirm == "yes" or Confirm == "y":
            Hold=Gen_FullName(Hold)
            Pila=Hold.split(" ",1)[0]
            Apellido=Hold.split(" ",1)[1]

            Mail=Gen_Mail(Mail_List,Pila,Apellido)
            Persona.extend([Hold,Mail,"A"])

            Num_list(Persona_ID)
            contador=len(Persona_ID)
            Aux[Persona_ID[contador-1]]=Persona
            Cliente.update(Aux)

        elif Confirm == "no" or Confirm == "n":
            input("Presione enter para volver al menu previo.")
            limpiar_pantalla()
            Flag=1

        else:
            limpiar_pantalla()
            print("Error, realice un ingreso valido")
            Flag=2
            

def Read_Cliente(Cliente): #Permite leer la matriz de clientes
                            #Para interfaz si quieren sacar el pretty print y poner otra cosa, no se va a romper
    pprint.pprint(Cliente)
    input("Presione enter para volver al menu previo.")
    limpiar_pantalla()
       

def Update_Cliente(Cliente): #Permite cambiar nombres de usuario pero si a alguien se le ocurre algun valor mas se le puede agregar
    Flag=0
    while Flag == 0:
        print()
        print("1) Modificar Nombre de Cliente")
        print("2) Modificar Apellido de Cliente")
        print("3) Modificar Nombre y Apellido de Cliente")
        print("4) Salir")
        Check= input(":")
        
        if Check=="1":
            Check,Search,Result=Verificacion_Mod_Usuario(Cliente)
            if Check=="y":
                print("A que quiere cambiar el nombre?")
                Gen_Nombre(Result)
                Cliente[Search]=Result
            
            elif Check =="n":
                Check="1"
                input("Presione enter para volver al menu previo.")
                limpiar_pantalla()
                pass
            else:
                limpiar_pantalla()
                print("Error,ingrese un input valido")
        
        elif Check=="2":
            Check,Search,Result=Verificacion_Mod_Usuario(Cliente)
            if Check=="y":
                print("A que quiere cambiar el nombre?")
                Gen_Apellido(Result)
                Cliente[Search]=Result
            
            elif Check =="n":
                Check="1"
                input("Presione enter para volver al menu previo.")
                limpiar_pantalla()
                pass
            else:
                limpiar_pantalla()
                print("Error,ingrese un input valido")
            
        elif Check=="3":
            Check,Search,Result=Verificacion_Mod_Usuario(Cliente)
            if Check=="y":
                print("A que quiere cambiar el nombre?")
                Gen_FullName(Result)
                Cliente[Search]=Result
            
            elif Check =="n":
                Check="1"
                input("Presione enter para volver al menu previo.")
                limpiar_pantalla()
                pass
            else:
                limpiar_pantalla()
                print("Error,ingrese un input valido")

        elif Check=="4":
            Flag=1
            input("Presione enter para volver al menu previo.")
            limpiar_pantalla()

        else:
            limpiar_pantalla()
            print("Error,ingrese un input valido")

    return Cliente

def Destruir_Cliente(Cliente):# Permite Borrar clientes
    Flag=0
    while Flag ==0:
        print("1)Borrar Cliente")
        print("2)Reactivar Cuenta")
        print("3)Salir")
        Check=input(":")
        if Check=="1":
            Check,Search,Result=Verificacion_Mod_Usuario(Cliente)
            if Check == "y":
                Cliente[Search][2]="IN"
                input("Presione enter para volver al menu previo.")
                limpiar_pantalla()
            
            elif Check =="n":
                Check="1"
                pass
            else:
                limpiar_pantalla()
                print("Error,ingrese un input valido")
        elif Check=="2":
            print("Ingrese el ID del cliente que quiere modificar, o Ingrese -1 para salir", end=" ")
            Search=input(":")
            if Search =="-1":
                limpiar_pantalla()
                return "n",0,0
            elif not Search.isnumeric():
                print("Error, ingrese un numero")
                return "n",0,0
            else:
                Search=int(Search)
                Result=Search_User(Search,Cliente)

                if Result=="Not Found":
                    print("Ese ID no esta en la base de datos")
                    return "n",0,0
                else:
                    print("Quiere modificar al cliente",Search,Result,"y/n",end=" ")
                    Check= input(":").strip()
                    
            if Check == "y":
                Cliente[Search][2]="A"
                input("Presione enter para volver al menu previo.")
                limpiar_pantalla()
            
            elif Check =="n":
                Check="1"
                pass
            else:
                limpiar_pantalla()
                print("Error,ingrese un input valido")
        
        elif Check=="3":
            Flag=1
            input("Presione enter para volver al menu previo.")
            limpiar_pantalla()

        else:
            limpiar_pantalla()
            print("Error,ingrese un input valido")

    return Cliente


Cliente,Persona_ID,Mail_List =Persona_Relleno()
limpiar_pantalla()
while True:
    print()
    print("Bienvenido!")
    print("Seleccione una opcion:")
    print("1) Crear Cliente")
    print("2) Leer Cliente")
    print("3) Modificar Cliente")
    print("4) Borrar Cliente")
    print("5) Salir")
    Check= input(":")
    if Check=="1":
        limpiar_pantalla()
        Crear_Cliente(Persona_ID,Cliente,Mail_List)
    
    elif Check =="2":
        limpiar_pantalla()
        Read_Cliente(Cliente)
    
    elif Check=="3":
        limpiar_pantalla()
        Update_Cliente(Cliente)
    
    elif Check=="4":
        limpiar_pantalla()
        Destruir_Cliente(Cliente)
    elif Check=="5":
        print("Bye!")
        Cleanup(Cliente,Persona_ID)
        break
    else :
        limpiar_pantalla()
        print("Error,ingrese un input valido") 