from empleados.usuarios import cargar_empleados
from empleados.constantes import USUARIO, NOMBRE, APELLIDO

def obtener_nombre_apellido(usuario):
    empleados = cargar_empleados()
    for empleado in empleados:
        if empleado[USUARIO] == usuario:
            return empleado[NOMBRE] + " " + empleado[APELLIDO]
    return ""