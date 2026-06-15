import os
import json

atributo_empleados = ["Id_empleado", "Nombre", "Apellido", "usuario", "Rol", "Contraseña", "Estado"]

# Ruta al archivo JSON de usuarios de manera relativa al archivo actual
ruta_json = os.path.join(os.path.dirname(__file__), "usuarios.json")

def cargar_empleados():
   
    #Carga la lista de empleados desde el archivo JSON.
    if not os.path.exists(ruta_json):
        #Si no existe podemos intentar crearlo con una lista vacía
        try:
            with open(ruta_json, 'w', encoding='utf-8') as archivo:
                json.dump([], archivo, ensure_ascii=False, indent=4)
        except Exception as error:
            print(f"Error al crear archivo JSON vacío: {error}")
        return []
    try:
        with open(ruta_json, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {ruta_json}.")
        return []
    except json.JSONDecodeError:
        print(f"Error: El archivo {ruta_json} tiene un formato JSON inválido.")
        return []
    except PermissionError:
        print(f"Error: Permiso denegado al intentar leer {ruta_json}.")
        return []
    except Exception as error:
        print(f"Error inesperado al cargar empleados: {error}")
        return []

def guardar_empleados(dic_empleados):
    
    #Guarda la lista de empleados en el archivo JSON.

    try:
        with open(ruta_json, 'w', encoding='utf-8') as archivo:
            json.dump(dic_empleados, archivo, ensure_ascii=False, indent=4)
        return True
    except PermissionError:
        print(f"Error: Permiso denegado al intentar escribir en {ruta_json}.")
        return False
    except OSError as error:
        print(f"Error de sistema/OS al escribir en {ruta_json}: {error}")
        return False
    except Exception as error:
        print(f"Error inesperado al guardar empleados: {error}")
        return False

empleados = cargar_empleados()
