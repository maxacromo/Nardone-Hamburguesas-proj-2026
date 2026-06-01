from empleados.usuarios import empleados
from empleados.constantes import USUARIO, NOMBRE, APELLIDO

def obtener_nombre_apellido(usuario):
    for empleado in empleados:
        if empleado[USUARIO] == usuario:
            return empleado[NOMBRE] + " " + empleado[APELLIDO]
    return ""