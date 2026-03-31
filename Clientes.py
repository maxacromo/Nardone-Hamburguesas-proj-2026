from Clientes_Funciones import *
import random, pprint

def Persona_Relleno(): #Genera Personas no reales para que el sistema cargue con usuarios ya existen
    Persona_ID=[]

    P_Random=random.randint(5,10)
    Persona=Creador_Personas(P_Random) 

    def Creador_Usuarios():
        Num_list(Persona,Persona_ID)
        Usuarios={}
        for i in range(len(Persona)):
            Usuarios[Persona_ID[i]]=Persona[i]
        return Usuarios
    

    Usuarios= Creador_Usuarios()
    return Usuarios, Persona_ID


def Crear_Cliente(Persona_ID,Usuarios): #Funcion que permite agregar usuarios
    Aux={}
    Hold=""
    Flag=0
    while Flag !=1:
        Flag=0
        Confirm=input("Quiere agregar un nuevo usuario? y/n:").strip()
        if Confirm == "yes" or Confirm == "y":
            Hold=Gen_Name(Hold)

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
            Usuarios.update(Aux)


 

def Read_Cliente(Usuarios): #Permite leer la matriz de clientes
                            #Para interfaz si quieren sacar el pretty print y poner otra cosa, no se va a romper
    pprint.pprint(Usuarios)
       

def Update_Cliente(Usuarios): #Permite cambiar nombres de usuario pero si a alguien se le ocurre algun valor mas se le puede agregar
    Flag=0
    while Flag == 0:
        print()
        print("1) Modificar Nombre de Usuario")
        print("2) Salir")
        Check= input(":")
        
        if Check=="1":
            Check,Search=Verificacion_Mod_Usuario(Usuarios)
            if Check=="y":
                print("A que quiere cambiar el nombre?")
                Change=""
                Change=Gen_Name(Change)
                Usuarios[Search]=Change
            
            elif Check =="n":
                Check="1"
                pass
            else:
                print("Error,ingrese un input valido")
        
        elif Check=="2":
            Flag=1

        else:
            print("Error,ingrese un input valido")

    return Usuarios

def Destruir_Cliente(Usuarios):# Permite Borrar clientes
    Flags=[]
    while 0 not in Flags:
        Flags.clear()
        Check=input("Quiere Borrar un cliente? y/n:")
        if Check=="y":
            Check,Search=Verificacion_Mod_Usuario(Usuarios)
            if Check == "y":
                Usuarios.pop(Search)
            
            elif Check =="n":
                Check="1"
                pass
            else:
                print("Error,ingrese un input valido")

        elif Check=="n":
            Flags.append(0)

        else:
            print("Error,ingrese un input valido")

    return Usuarios


Usuarios,Persona_ID =Persona_Relleno()

while True:
    print()
    print("Bienvenido!")
    print("Seleccione una opcion:")
    print("1) Crear Usuario")
    print("2) Leer Usuario")
    print("3) Modificar Usuario")
    print("4) Borrar Usuario")
    print("5) Salir")
    Check= input(":")
    if Check=="1":
        Crear_Cliente(Persona_ID,Usuarios)
    
    elif Check =="2":
        Read_Cliente(Usuarios)
    
    elif Check=="3":
        Update_Cliente(Usuarios)
    
    elif Check=="4":
        Usuarios = Destruir_Cliente(Usuarios)
    elif Check=="5":
        print("Bye!")
        break
    else :
        print("Error,ingrese un input valido") 