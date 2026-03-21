import os
import time

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def dibujar_borde(titulo, ancho=60):
    print("╔" + "═" * (ancho-2) + "╗")
    print("║" + titulo.center(ancho-2) + "║")
    print("╚" + "═" * (ancho-2) + "╝")
    print()

def menu_principal():
    while True:
        limpiar()
        dibujar_borde(" HAMBURGESAS ", 40)
        print("  1. Iniciar sesión")
        print("  2. Registrarse")
        print("  3. Ver créditos")
        print("  4. Salir")
        print()
        
        opcion = input("  → Elige una opción (1-4): ").strip()

        #opcion de menu
        if opcion == "1":
            login()
        elif opcion == "2":
            registro()
        elif opcion == "3":
            limpiar()
            dibujar_borde(" CRÉDITOS ", 40)
            print("  Hecho por Hernan el Crack")
            input("\n  Presiona Enter para volver...")
        elif opcion == "4":
            print("\n  Nos vemos nene, cuidate")
            time.sleep(1)
            break
        else:
            print("  Opción inválida... intenta de nuevo")
            time.sleep(1.5)

def login():
    limpiar()
    dibujar_borde(" INICIAR SESIÓN ", 40)
    usuario = input("  Usuario: ").strip()
    contra = input("  Contraseña: ").strip()  
    
    # Simulación simple
    if usuario == "hernan" and contra == "1234":
        print("\n  ¡Bienvenido Hernan!")

    elif usuario == "keni" and contra == "1234":
        print("\n  ¡Bienvenido Hernan!")
    
    elif usuario == "juan" and contra == "1234":
        print("\n  ¡Bienvenido Hernan!")

    else:
        print("\n  Usuario o contraseña incorrectos ✗")
    input("\n  Presiona Enter para continuar...")

#gay el que lee

def registro():
    limpiar()
    dibujar_borde(" REGISTRARSE ", 40)
    print("  (Funcionalidad simulada – no guarda nada)")
    input("  Presiona Enter para volver...")

# Inicio del programa
print("Cargando sistema...")
time.sleep(1.2)
menu_principal()

