from Clientes_Funciones import *
import random, pprint

def Persona_Relleno(): #Genera Personas no reales para que el sistema cargue con usuarios ya existen
    Persona_ID=[]

    P_Random=random.randint(5,10)
    Persona=Creador_Personas(P_Random) 

    def Creador_Usuarios():
        Num_list(Persona,Persona_ID)
        Usuarios=[]
        for i in range(len(Persona)):
            user=[(Persona_ID[i]),Persona[i]]
            Usuarios.append(user)
        return Usuarios
    

    Usuarios= Creador_Usuarios()
    return Usuarios, Persona_ID


def Crear_Cliente(Persona_ID,Usuarios): #Funcion que permite agregar usuarios
    Persona=[]
    Persona.extend(Usuarios)
    Hold=[]
    contador=len(Persona_ID)
    Flag=0
    while Flag ==0:
        Confirm=input("Quiere agregar un nuevo usuario? y/n:").strip()
        if Confirm == "yes" or Confirm == "y":
            Gen_Name(Hold)

        elif Confirm == "no" or Confirm == "n":
            Flag=1

        else:
            print("Error, realice un ingreso valido")


    for i in range(len(Hold)):
            nro=-1
            flag=0
            while flag==0:
                if nro in Persona_ID or nro==-1:
                    nro=random.randint(100000,999999)
                else:
                    Persona_ID.append(nro)
                    flag=1
    
    for i in range(len (Hold)):
        Aux=[Persona_ID[i+contador],Hold[i]]
        Persona.append(Aux) #Une los ids con los nombres

    return Persona
 

def Read_Cliente(Usuarios): #Permite leer la matriz de clientes
                            #Para interfaz si quieren sacar el pretty print y poner otra cosa, no se va a romper
    pprint.pprint(Usuarios)
       

def Update_Cliente(Usuarios): #Permite cambiar nombres de usuario pero si a alguien se le ocurre algun valor mas se le puede agregar
    Flag=0
    while Flag == 0:
        print()
        print("1) Modificar Nombre de Usuario")
        print("2) Modificar ID de Usuario")
        print("3) Salir")
        Check= input(":")
        
        if Check=="1":
            Check,cont=Verificacion_Mod_Usuario(Usuarios)
            if Check=="y":
                print("A que quiere cambiar el nombre?")
                Change=""
                Gen_Name(Change)
                Usuarios[cont][1]=Change
            
            elif Check =="n":
                Check="1"
                pass
            else:
                print("Error,ingrese un input valido")
        
        elif Check=="2":
            Check,cont=Verificacion_Mod_Usuario(Usuarios)
            if Check=="y":
                Change=int(input("Ingrese el nuevo ID del usuario:"))
                Usuarios[cont][0]=Change
            
            elif Check =="n":
                Check="1"
                pass
            else:
                print("Error,ingrese un input valido")
        
        elif Check=="3":
            Flag=1

        else:
            print(" No <3")

    return Usuarios

def Destruir_Cliente(Usuarios):# Permite Borrar clientes
    Flags=[]
    while 0 not in Flags:
        Flags.clear()
        Check=input("Quiere Borrar un cliente? y/n:")
        if Check=="y":
            Check,cont=Verificacion_Mod_Usuario(Usuarios)
            if Check == "y":
                Usuarios.pop(cont)
            
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
        Usuarios = Crear_Cliente(Persona_ID,Usuarios)
    
    elif Check =="2":
        Read_Cliente(Usuarios)
    
    elif Check=="3":
        Usuarios = Update_Cliente(Usuarios)
    
    elif Check=="4":
        Usuarios = Destruir_Cliente(Usuarios)
    elif Check=="5":
        print("Bye!")
        break
    else :
        print("Nop :3") 