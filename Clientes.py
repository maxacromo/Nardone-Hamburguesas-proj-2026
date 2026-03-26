import random, pprint

def Persona_Relleno():
    Persona_ID=[]
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

    P_Random=random.randint(25,30)
    Persona=Creador_Personas(P_Random) 

    def Num_list():# Crea ID de Usuario
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

    
                    

    def Creador_Usuarios():
        Num_list()
        Usuarios=[]
        for i in range(len(Persona)):
            user=[(Persona_ID[i]),Persona[i]]
            Usuarios.append(user)
        return Usuarios
    

    Usuarios= Creador_Usuarios()
    return Usuarios, Persona_ID

def Gen_Name (Aux):#Se utiliza para 
    while True:
        Pila=input("Inserte el nombre de pila del Usuario:")
        Apellido=input("Inserte el Apellido del Usuario:")
        Nombre= Pila+" "+Apellido
        print("Su nombre es ", Nombre, "? y/n", end=" ")
        Confirm=input(":").strip()
        print()

        if Confirm == "yes" or Confirm == "y":
            Aux.append(Nombre)
            break

        elif Confirm == "no" or Confirm == "n":
            break

        else:
            print("Error, realice un ingreso valido")
    return Aux

def Search_User(Search):#Ubica las posciciones del id de los usuarios
    cont=0
    Result= Search in Usuarios[cont]
    while Result == False and cont != len(Usuarios)-1:
        cont +=1
        Result= Search in Usuarios[cont]
    return Result, cont

def Crear_Cliente(Persona_ID): #Funcion que permite agregar usuarios
    Persona=[]
    Persona.extend(Usuarios)
    Hold=[]
    contador=len(Persona_ID)

    while True:
        Confirm=input("Quiere agregar un nuevo usuario? y/n:").strip()
        if Confirm == "yes" or Confirm == "y":
            Gen_Name(Hold)

        elif Confirm == "no" or Confirm == "n":
            break

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
    Flags=[]
    while 0 not in Flags:
        Flags.clear()
        print()
        print("1) Modificar Nombre de Usuario")
        print("2) Salir")
        Check= input(":")
        
        if Check=="1":
            print("Ingrese el ID del usuario cuyo nombre quiere modificar, o Ingrese -1 para salir", end=" ")
            Search=int(input(":"))
            if Search ==-1:
                pass
            Result,cont=Search_User(Search)


            if Result ==True:
                while 1 not in Flags:
                    print("Quiere cambiarle el nombre al usuario",Usuarios[cont],"y/n",end=" ")
                    Check= input(":").strip()
                    if Check=="y":
                        Hold=[]
                        print("A que quiere cambiar el nombre?")
                        Gen_Name(Hold)
                        Change=Hold[0]
                        Usuarios[cont][1]=Change
                        Flags.append(1)
            
                    elif Check =="n":
                        Flags.append(1)
                    else:
                        print("Error,ingrese un input valido")
                    
            else:
                print("Ese ID no esta en la base de datos")
                    
        
        elif Check=="2":
            Flags.append(0)

        else:
            print(" No <3")

    return Usuarios

def Destruir_Cliente(Usuarios):# Permite Borrar clientes
    Flags=[]
    while 0 not in Flags:
        Flags.clear()
        Check=input("Quiere Borrar un cliente? y/n:")
        if Check=="y":
            print("Ingrese el ID del usuario cuyo nombre quiere modificar, o Ingrese -1 para salir:", end=" ")
            Search=int(input(":"))
            if Search ==-1:
                pass
            else:
                Result,cont=Search_User(Search)

                if Result ==True:
                    while 1 not in Flags:
                        print("Quiere borrar al usuario",Usuarios[cont],"y/n")
                        Check= input(":").strip()
                        if Check=="y":
                            Usuarios.pop(cont)
                            Flags.append(1)
                
                        elif Check =="n":
                            Flags.append(1)
                            
                        else:
                            print("Error,ingrese un input valido")

                else:
                    print("Ese ID no esta en la base de datos")

        elif Check=="n":
            Flags.append(0)

        else:
            print("Error,ingrese un input valido")

    return Usuarios


Usuarios,Persona_ID =Persona_Relleno()

while True:
    print()
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
        Usuarios = Crear_Cliente(Persona_ID)
    
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
