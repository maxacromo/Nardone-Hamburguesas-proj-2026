from funciones import menu_admin
from usuarios import empleados, atributo_empleados

def main():
    print("Bienvenidos al sistema de administración")
    menu_admin(empleados, atributo_empleados)

if __name__ == "__main__":
    main()