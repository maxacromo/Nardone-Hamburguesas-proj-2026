import random, pprint


def Fake_Faker():
    def Creador_Personas(cycle): #Esta funcion toma un nombre y un apellido de las listas para generar a una persona con un nombre aleatorio
                                #Además Carga a las personas a una lista q luego es pasada a otra lista en el llamado de función 
        cont=0
        Personas=[]

        while cont != cycle:
            Pila=["María","Ana","Lucia","Martina","Daniela","Jose","Luis","Carlos","Juan","Martin"]
            Apellidos=["González", "Rodríguez", "Gómez", "Fernández", "López", "Martínez", "Díaz", "Pérez", "Sánchez", "Romero"]

            Personas.append(Pila[random.randint(0,len(Pila)-1)]+" "+ Apellidos[random.randint(0,len(Apellidos)-1)])
            cont+=1

        return Personas

    Personas=Creador_Personas(int(input("Cuantas Personas quiere generar?:"))) 

    def Num_list():
        Usado=[]
        for i in range(len(Personas)):
            nro=-1
            while True:
                if nro in Usado or nro==-1:
                    nro=random.randint(100000,999999)
                else:
                    Usado.append(nro)
                    break
        return Usado


    def Creador_Usuarios():
        Usado=Num_list()
        Pedidos=["Placeholder_Combo_1","Placeholder_Combo_2","Placeholder_Combo_3"]
        Usuarios=[]
        for i in range(len(Personas)):
            ped_rand=random.randint(0,len(Pedidos)-1)
            user=[str(Usado[i])+" "+Personas[i]+" "+Pedidos[ped_rand]]
            Usuarios.append(user)
        return Usuarios

    Usuarios=Creador_Usuarios()

    pprint.pprint(Usuarios)
        
Fake_Faker()    