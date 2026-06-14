import os
from empleados.usuarios import empleados

def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def obtener_nombre_apellido(usuario):
    for empleado in empleados:
        if empleado[3] == usuario:
            return empleado[1] + " " + empleado[2]
    return ""