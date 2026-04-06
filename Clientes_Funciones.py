import random

def Creador_Personas(cycle): #Esta funcion toma un nombre y un apellido de las listas para generar a una persona con un nombre aleatorio
                                 #Además Carga a las personas a una lista q luego es pasada a otra lista en el llamado de función 
        cont=0
        Persona=[]
        Random_Names=lambda: random.choice(Pila) + " " + random.choice(Apellidos)

        while cont != cycle:
            Pila=["María","Ana","Lucia","Martina","Daniela","Julia","Luciana","Sofia", "Jose","Luis","Carlos","Juan","Martin","Julian","Esteban","Roberto"]
            Apellidos=["González","Rodríguez","Gómez","Fernández","López","Díaz","Martínez","Pérez","Sánchez","Romero","García","Sosa","Benítez","Ramírez","Ruiz","Torres"]

        
            Persona.append(Random_Names())
            cont+=1

        return Persona

def Num_list(Persona,Persona_ID):# Crea ID de Usuario para las personas de relleno
        for i in range(len(Persona)):
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

def Gen_FullName (Fullname):#Se utiliza para el input de nombres de parte de los usuarioss
    Flag=0
    while Flag==0:
        Pila=input("Inserte el nombre de pila del cliente:")
        Apellido=input("Inserte el Apellido del cliente:")
        Nombre= Pila+" "+Apellido
        print("Su nombre es ", Nombre, "? y/n", end=" ")
        Confirm=input(":").strip()
        print()

        if Confirm == "yes" or Confirm == "y":
            Fullname=Nombre
            Flag=1

        elif Confirm == "no" or Confirm == "n":
            Flag=1

        else:
            print("Error, realice un ingreso valido")
    return Fullname

def Gen_Nombre (Aux,Result):#Se utiliza para el input de nombres de parte de los Cliente
    Flag=0
    while Flag==0:
        Pila=input("Inserte el nombre de pila del cliente:")
        Nombre= Pila + " " + Result.split(" ",1)[1]
        print("Su nombre es ", Nombre, "? y/n", end=" ")
        Confirm=input(":").strip()
        print()

        if Confirm == "yes" or Confirm == "y":
            Aux=Nombre
            Flag=1

        elif Confirm == "no" or Confirm == "n":
            Aux=Result
            Flag=1

        else:
            print("Error, realice un ingreso valido")
    return Aux

def Gen_Apellido (Aux,Result):#Se utiliza para el input de nombres de parte de los Cliente
    Flag=0
    while Flag==0:
        Apellido=input("Inserte el apellido del cliente:")
        Nombre= Result.split(" ",1)[0] + " " + Apellido
        print("Su nombre es ", Nombre, "? y/n", end=" ")
        Confirm=input(":").strip()
        print()

        if Confirm == "yes" or Confirm == "y":
            Aux=Nombre
            Flag=1

        elif Confirm == "no" or Confirm == "n":
            Aux=Result
            Flag=1

        else:
            print("Error, realice un ingreso valido")
    return Aux 


def Search_User(Search,Cliente):#Ubica las posciciones del id de los Cliente
    print(Cliente[Search])
    if Search in Cliente:
        print("Found")
        Result=Cliente[Search]
        return Result
    else:
        Result="Not Found"
        return Result


def Verificacion_Mod_Usuario(Cliente):
    print("Ingrese el ID del cliente que quiere modificar, o Ingrese -1 para salir", end=" ")
    Search=input(":")
    if not Search.isdigit():
        print("Error, ingrese un numero")
        return "n",0,0
    else:
        Search=int(Search)
        if Search ==-1:
            return "n",0,0
        Result=Search_User(Search,Cliente)

        if Result=="Not Found":
            print("Ese ID no esta en la base de datos")

        else:
            print("Quiere modificar al cliente",Search,Result,"y/n",end=" ")
            Check= input(":").strip()
            return Check, Search, Result
