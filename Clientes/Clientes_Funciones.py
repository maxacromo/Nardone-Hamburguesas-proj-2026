import random, os,json


def Num_list(Persona_ID):# Crea ID de Usuario para las personas de relleno
            nro=-1
            flag=0
            Check_ID=lambda x: False if x in Persona_ID else True
            while flag==0 :
                if Check_ID== False or nro==-1:
                    nro=random.randint(100000,999999)
                    Check_ID(nro)
                else:
                    nro=str(nro)
                    Persona_ID.append(nro)
                    flag=1

def Gen_FullName (Result,yesno):#Se utiliza para el input de nombres de parte de los usuarioss
    Flag=0
    while Flag==0:
        try:
            Pila=input("Inserte el nombre de pila del cliente:")
            Apellido=input("Inserte el Apellido del cliente:")
            Nombre= Pila+" "+Apellido
            if len(Pila)> 12:
                raise ValueError("Su nombre debe ser menor a 12 caracteres")
            elif len(Apellido)>12:
                raise ValueError("Su nombre debe ser menor a 12 caracteres")
            elif not Nombre.strip():
                raise ValueError("Su nombre no puede estar vacio")
            elif not Nombre.replace(" ", "").isalpha():
                raise ValueError("Su nombre no puede contener numeros")
        except ValueError as error :
            print("Error:",error)
            input("Presione enter para volver al menu previo.")
            limpiar_pantalla()
            continue

        print("Su nombre es ", Nombre, "? y/n", end=" ")
        try:
            Confirm=input(":").strip().lower()
            if Confirm.isnumeric()or Confirm not in yesno:
                raise ValueError("Ingreso no valido")

        except ValueError as error:
            print("Error:",error)
            input("Presione enter para volver al menu previo.")
            limpiar_pantalla()
        print()

        if Confirm == "yes" or Confirm == "y":
            Result=Nombre
            Flag=1

        elif Confirm == "no" or Confirm == "n":
            Flag=1


    return Result

def Gen_Nombre (Result,yesno):#Se utiliza para el input de nombres de parte de los Cliente
    Flag=0
    while Flag==0:
        try:
            Pila=input("Inserte el nombre de pila del cliente:")
            if len(Pila)> 12:
                raise ValueError("Su nombre debe ser menor a 12 caracteres")
            elif not Pila.strip():
                raise ValueError("Su nombre no puede estar vacio")
            elif not Pila.replace(" ", "").isalpha():
                raise ValueError("Su nombre no puede contener numeros")
        except ValueError as error :
            print("Error:",error)
            input("Presione enter para volver al menu previo.")
            limpiar_pantalla()
            continue            
        Apellido=Result[0].split(" ",1)[1]
        Nombre= Pila + " " + Apellido
        print("Su nombre es ", Nombre, "? y/n", end=" ")
        try:
            Confirm=input(":").strip().lower()
            if Confirm.isnumeric()or Confirm not in yesno:
                raise ValueError("Ingreso no valido")

        except ValueError as error:
            print("Error:",error)
            input("Presione enter para volver al menu previo.")
            limpiar_pantalla()

        input("Presione enter para volver al menu previo.")
        limpiar_pantalla()

        if Confirm == "yes" or Confirm == "y":
            Result[0]=Nombre
            Flag=1

        elif Confirm == "no" or Confirm == "n":
            print("Error:",error)
            input("Presione enter para volver al menu previo.")
            Flag=1

    return Result

def Gen_Apellido (Result,yesno):#Se utiliza para el input de nombres de parte de los Cliente
    Flag=0
    while Flag==0:
        Pila=Result[0].split(" ",1)[0]
        try:
            Apellido=input("Inserte el apellido del cliente:")
            if len(Apellido)>12:
                raise ValueError("Su nombre debe ser menor a 12 caracteres")
            elif not Apellido.strip():
                raise ValueError("Su nombre no puede estar vacio")
            elif not Apellido.replace(" ", "").isalpha():
                raise ValueError("Su nombre no puede contener numeros")
        except ValueError as error :
            print("Error:",error)
            input("Presione enter para volver al menu previo.")
            limpiar_pantalla()
            continue

        Nombre= Pila + " " + Apellido
        print("Su nombre es ", Nombre, "? y/n", end=" ")
        try:
            Confirm=input(":").strip().lower()
            if Confirm.isnumeric()or Confirm not in yesno:
                raise ValueError("Ingreso no valido")

        except ValueError as error:
            print("Error:",error)
            input("Presione enter para volver al menu previo.")
            limpiar_pantalla()
        print()

        if Confirm == "yes" or Confirm == "y":
            Result[0]=Nombre
            Flag=1

        elif Confirm == "no" or Confirm == "n":
            Flag=1

    return Result


def Search_Client_ID(Search,Cliente):#Ubica las posciciones del id de los Cliente
    if Search in Cliente:
        Result=Cliente[Search]
        return Result
    else:
        Result="Not Found"
        return Result


def Verificacion_Mod_Usuario(Cliente,yesno,Restore):
    while True:
        try:
            Search=input("Ingrese el ID del cliente que quiere modificar, o Ingrese 0 para salir:")
            if Search=="0":
                input("Presione enter para volver al menu previo.")
                limpiar_pantalla()
                return "n",0,0
            
            elif Search.replace(" ","").isalpha():
                raise ValueError("El ID no puede contener letras")

            elif not Search:
                raise ValueError("El ID no puede ser vacio")
            else:
                break
            

        except ValueError as error:
                print("Error:",error)
                input("Presione enter para volver al menu previo.")
                limpiar_pantalla()    
    if Search ==0:
        input("Presione enter para volver al menu previo.")
        limpiar_pantalla()
        return "n",0,0
    else:
        Result=Search_Client_ID(Search,Cliente)

        if Result=="Not Found":
            print("Ese ID no esta en la base de datos")
            input("Presione enter para volver al menu previo.")
            limpiar_pantalla()
            return "n",0,0
        
        elif Result[2]==False and Restore==0:
            print("Esta cuenta esta inactiva")
            return "n",0,0

        else:
            print("Quiere modificar al cliente",Search,Result,"y/n",end=" ")
        try:
            Check=input(":").strip().lower()
            if Check.isnumeric()or Check not in yesno:
                raise ValueError("Ingreso no valido")

        except ValueError as error:
            print("Error:",error)
            input("Presione enter para volver al menu previo.")
            limpiar_pantalla()

        if Check == "yes" or Check== "y":
            return Check, Search, Result
        
        elif Check== "no" or Check== "n":
            input("Presione enter para volver al menu previo.")
            limpiar_pantalla()
            return "n",0,0

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
    Cliente_Usuario=Mail_Root+str(cont)
    return Mail,Cliente_Usuario

def Cleanup(Cliente,Persona_ID):
    for i in range(len(Persona_ID)):
        if False in Cliente[Persona_ID[i]]:
            Cliente.pop(Persona_ID[i])

def Update_Client_File(Cliente):
    try:
        with open("Clientes_Datos.json","w",encoding="UTF-8")as Datos:
            json.dump(Cliente,Datos,indent=4)

    except(FileNotFoundError,OSError) as error:
        print("Error:",error)


def Search_Client_Name(Search,Cliente,Persona_ID):

    for i in range(len(Persona_ID)):
        if Search in Cliente[Persona_ID[i]]:
            Result=Persona_ID[i]
            return Result

    
    Result="Not Found"
    return Result