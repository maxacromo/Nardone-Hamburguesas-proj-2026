from Clientes_Funciones import *
import random, pprint

def Persona_Relleno(): #Genera Personas no reales para que el sistema cargue con Cliente ya existen
    Persona_ID=[]

    P_Random=random.randint(5,10)
    Persona=Creador_Personas(P_Random) 

    def Creador_Usuarios():
        Num_list(Persona,Persona_ID)
        Cliente={}
        for i in range(len(Persona)):
            Cliente[Persona_ID[i]]=Persona[i]
        return Cliente
    

    Cliente= Creador_Usuarios()
    return Cliente, Persona_ID


def Crear_Cliente(Persona_ID,Cliente): #Funcion que permite agregar Cliente
    Aux={}
    Hold=""
    Flag=0
    while Flag !=1:
        Flag=0
        Confirm=input("Quiere agregar un nuevo cliente? y/n:").strip()
        if Confirm == "yes" or Confirm == "y":
            Hold=Gen_FullName(Hold)

        elif Confirm == "no" or Confirm == "n":
            Flag=1

        else:
            print("Error, realice un ingreso valido")
            Flag=2
            


        if Flag==1 or Flag==2:
            pass
        else:
            nro=-1
            flag=0
            while flag==0:
                if nro in Persona_ID or nro==-1:
                    nro=random.randint(100000,999999)
                else:
                    Persona_ID.append(nro)
                    flag=1
            contador=len(Persona_ID)
            Aux[Persona_ID[contador-1]]=Hold
            Cliente.update(Aux)


 

def Read_Cliente(Cliente): #Permite leer la matriz de clientes
                            #Para interfaz si quieren sacar el pretty print y poner otra cosa, no se va a romper
    pprint.pprint(Cliente)
       

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
                Change=""
                Change=Gen_Nombre(Change,Result)
                Cliente[Search]=Change
            
            elif Check =="n":
                Check="1"
                pass
            else:
                print("Error,ingrese un input valido")
        
        elif Check=="2":
            Check,Search,Result=Verificacion_Mod_Usuario(Cliente)
            if Check=="y":
                print("A que quiere cambiar el nombre?")
                Change=""
                Change=Gen_Apellido(Change,Result)
                Cliente[Search]=Change
            
            elif Check =="n":
                Check="1"
                pass
            else:
                print("Error,ingrese un input valido")
            
        elif Check=="3":
            Check,Search,Result=Verificacion_Mod_Usuario(Cliente)
            if Check=="y":
                print("A que quiere cambiar el nombre?")
                Change=""
                Change=Gen_FullName(Change)
                Cliente[Search]=Change
            
            elif Check =="n":
                Check="1"
                pass
            else:
                print("Error,ingrese un input valido")

        elif Check=="4":
            Flag=1

        else:
            print("Error,ingrese un input valido")

    return Cliente

def Destruir_Cliente(Cliente):# Permite Borrar clientes
    Flags=[]
    while 0 not in Flags:
        Flags.clear()
        Check=input("Quiere Borrar un cliente? y/n:")
        if Check=="y":
            Check,Search=Verificacion_Mod_Usuario(Cliente)
            if Check == "y":
                Cliente.pop(Search)
            
            elif Check =="n":
                Check="1"
                pass
            else:
                print("Error,ingrese un input valido")

        elif Check=="n":
            Flags.append(0)

        else:
            print("Error,ingrese un input valido")

    return Cliente


Cliente,Persona_ID =Persona_Relleno()

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
        Crear_Cliente(Persona_ID,Cliente)
    
    elif Check =="2":
        Read_Cliente(Cliente)
    
    elif Check=="3":
        Update_Cliente(Cliente)
    
    elif Check=="4":
        Cliente = Destruir_Cliente(Cliente)
    elif Check=="5":
        print("Bye!")
        break
    else :
        print("Error,ingrese un input valido") 