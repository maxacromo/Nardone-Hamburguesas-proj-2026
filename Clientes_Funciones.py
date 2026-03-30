import random

def Creador_Personas(cycle): #Esta funcion toma un nombre y un apellido de las listas para generar a una persona con un nombre aleatorio
                                 #Además Carga a las personas a una lista q luego es pasada a otra lista en el llamado de función 
        cont=0
        Persona=[]

        while cont != cycle:
            Pila=["María","Ana","Lucia","Martina","Daniela","Julia","Luciana","Sofia", "Jose","Luis","Carlos","Juan","Martin","Julian","Esteban","Roberto"]
            Apellidos=["González","Rodríguez","Gómez","Fernández","López","Díaz","Martínez","Pérez","Sánchez","Romero","García","Sosa","Benítez","Ramírez","Ruiz","Torres"]

            Persona.append(Pila[random.randint(0,len(Pila)-1)]+" "+ Apellidos[random.randint(0,len(Apellidos)-1)])
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

def Gen_Name (Aux):#Se utiliza para el input de nombres de parte de los usuarios
    Flag=0
    while Flag==0:
        Pila=input("Inserte el nombre de pila del Usuario:")
        Apellido=input("Inserte el Apellido del Usuario:")
        Nombre= Pila+" "+Apellido
        print("Su nombre es ", Nombre, "? y/n", end=" ")
        Confirm=input(":").strip()
        print()

        if Confirm == "yes" or Confirm == "y":
            Aux.append(Nombre)
            Flag=1

        elif Confirm == "no" or Confirm == "n":
            Flag=1

        else:
            print("Error, realice un ingreso valido")
    return Aux

def Search_User(Search,Usuarios):#Ubica las posciciones del id de los usuarios
    cont=0
    Result= Search in Usuarios[cont]
    while Result == False and cont != len(Usuarios)-1:
        cont +=1
        Result= Search in Usuarios[cont]
    return Result, cont

def Verificacion_Mod_Usuario(Usuarios):
    print("Ingrese el ID del usuario que quiere modificar, o Ingrese -1 para salir", end=" ")
    Search=int(input(":"))
    if Search ==-1:
        return "n",0
    Result,cont=Search_User(Search,Usuarios)

    if Result ==True:
        print("Quiere modificar al usuario",Usuarios[cont],"y/n",end=" ")
        Check= input(":").strip()
        return Check,cont

                    
    else:
        print("Ese ID no esta en la base de datos")