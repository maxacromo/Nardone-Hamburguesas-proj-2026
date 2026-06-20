import os
from empleados.usuarios import cargar_empleados
from empleados.constantes import USUARIO, NOMBRE, APELLIDO

def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def obtener_nombre_apellido(usuario):
    empleados = cargar_empleados()
    for empleado in empleados:
        if empleado[USUARIO] == usuario:
            return empleado[NOMBRE] + " " + empleado[APELLIDO]
    return ""