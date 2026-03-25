from funciones import agregar_empleado, mostrar_empleados, modificar_usuario
atributo_empleados=["Id_empleado","Nombre","Apellido","usuario","Rol"]
matriz_empleados=agregar_empleado()
mostrar_empleados(matriz_empleados,atributo_empleados)#Ya me muestra la matriz por el for que tiene la funcion.
modificar_usuario(matriz_empleados)
mostrar_empleados(matriz_empleados,atributo_empleados)

                                           