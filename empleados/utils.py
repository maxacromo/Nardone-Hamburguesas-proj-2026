from empleados.usuarios import empleados

def obtener_nombre_apellido(usuario):
    for empleado in empleados:
        if empleado[3] == usuario:
            return empleado[1] + " " + empleado[2]
    return ""