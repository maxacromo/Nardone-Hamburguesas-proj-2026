import random, os

def Creador_Personas(Mail_List): #Esta funcion toma un nombre y un apellido de las listas para generar a una persona con un nombre aleatorio
                                 #Además Carga a las personas a una lista q luego es pasada a otra lista en el llamado de función      
    Persona=[]
    L_Pila=["María","Ana","Lucia","Martina","Daniela","Julia","Luciana","Sofia", "Jose","Luis","Carlos","Juan","Martin","Julian","Esteban","Roberto"]
    L_Apellidos=["González","Rodríguez","Gómez","Fernández","López","Díaz","Martínez","Pérez","Sánchez","Romero","García","Sosa","Benítez","Ramírez","Ruiz","Torres"]

    Pila=random.choice(L_Pila) 
    Apellido=random.choice(L_Apellidos)
    Nombre=Pila+" "+Apellido
    Mail=Gen_Mail(Mail_List,Pila,Apellido)
    Persona.extend([Nombre,Mail,"A"])

    return Persona


def Num_list(Persona_ID):# Crea ID de Usuario para las personas de relleno
            nro=-1
            flag=0
            Check_ID=lambda x: False if x in Persona_ID else True
            while flag==0 :
                if Check_ID== False or nro==-1:
                    nro=random.randint(100000,999999)
                    Check_ID(nro)
                else:
                    Persona_ID.append(nro)
                    flag=1

def Gen_FullName (Result):#Se utiliza para el input de nombres de parte de los usuarioss
    Flag=0
    while Flag==0:
        Pila=input("Inserte el nombre de pila del cliente:")
        Apellido=input("Inserte el Apellido del cliente:")
        Nombre= Pila+" "+Apellido
        print("Su nombre es ", Nombre, "? y/n", end=" ")
        Confirm=input(":").strip()
        print()

        if Confirm == "yes" or Confirm == "y":
            Result[0]=Nombre
            Flag=1

        elif Confirm == "no" or Confirm == "n":
            Flag=1

        else:
            limpiar_pantalla()
            print("Error, realice un ingreso valido")
    return Result

def Gen_Nombre (Result):#Se utiliza para el input de nombres de parte de los Cliente
    Flag=0
    while Flag==0:
        Pila=input("Inserte el nombre de pila del cliente:")
        Apellido=Result[0].split(" ",1)[1]
        Nombre= Pila + " " + Apellido
        print("Su nombre es ", Nombre, "? y/n", end=" ")
        Confirm=input(":").strip()
        print()

        if Confirm == "yes" or Confirm == "y":
            Result[0]=Nombre
            Flag=1

        elif Confirm == "no" or Confirm == "n":
            Flag=1

        else:
            print("Error, realice un ingreso valido")
    return Result

def Gen_Apellido (Result):#Se utiliza para el input de nombres de parte de los Cliente
    Flag=0
    while Flag==0:
        Pila=Result[0].split(" ",1)[0]
        Apellido=input("Inserte el apellido del cliente:")
        Nombre= Pila + " " + Apellido
        print("Su nombre es ", Nombre, "? y/n", end=" ")
        Confirm=input(":").strip()
        print()

        if Confirm == "yes" or Confirm == "y":
            Result[0]=Nombre
            Flag=1

        elif Confirm == "no" or Confirm == "n":
            Flag=1

        else:
            print("Error, realice un ingreso valido")
    return Result


def Search_User(Search,Cliente):#Ubica las posciciones del id de los Cliente
    if Search in Cliente:
        Result=Cliente[Search]
        return Result
    else:
        Result="Not Found"
        return Result


def Verificacion_Mod_Usuario(Cliente):
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
        
        elif Result[2]=="IN":
            print("Esta cuenta esta inactiva")
            return "n",0,0

        else:
            print("Quiere modificar al cliente",Search,Result,"y/n",end=" ")
            Check= input(":").strip()
            return Check, Search, Result

def limpiar_pantalla():
    if os.name == "nt":  # Windows
        #Es una funcion de python que ejecuta comandos del sistema operativo.
        os.system("cls")#Le pasamos el comando y lo ejectua en la shell
    else: #Liempia la pantalla Linux y Mac
        os.system("clear")

Lowercase= lambda x: x.lower()

def Gen_Mail(Mail_List,Pila,Apellido):
    Mail_Root=Lowercase(Pila)[:1]+Lowercase(Apellido)
    Mailatt="@gmail.com"
    Mail=Mail_Root+Mailatt
    cont=1
    while Mail in Mail_List:
        cont=str(cont)
        Mail=Mail_Root+cont+Mailatt
        cont=int(cont)
        cont+=1
    Mail_List.append(Mail)
    return Mail

def Cleanup(Cliente,Persona_ID):
    for i in range(len(Persona_ID)):
        if "IN" in Cliente[Persona_ID[i]]:
            Cliente.pop(Persona_ID[i])