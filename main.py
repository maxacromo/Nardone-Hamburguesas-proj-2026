
from empleados.funciones import menu_principal
from empleados.usuarios import empleados, atributo_empleados

def main():
    print("Bienvenidos al sistema de administración")
    menu_principal(empleados, atributo_empleados)

if __name__ == "__main__":
    main()
