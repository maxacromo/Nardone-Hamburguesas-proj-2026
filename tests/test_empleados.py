import pytest
from empleados.funciones import buscar_usuario_secuencial, existe_usuario, obtener_id
from empleados.constantes import ID_EMPLEADO, USUARIO, PASSWORD, ESTADO, NOMBRE, APELLIDO, ROL

@pytest.fixture
def empleados_prueba():
    #Datos de prueba
    empleados_p = [
        {
            ID_EMPLEADO: 1,
            NOMBRE: "Juan",
            APELLIDO: "Perez",
            USUARIO: "juan123",
            ROL: "empleado",
            PASSWORD: "pass123",
            ESTADO: "Activo"
        },
        {
            ID_EMPLEADO: 2,
            NOMBRE: "Ana",
            APELLIDO: "Gomez",
            USUARIO: "ana456",
            ROL: "admin",
            PASSWORD: "adminpass",
            ESTADO: "Inactivo"
        }
    ]
    return empleados_p

def test_busquedaSecuencial(empleados_prueba):
    #Busqueda secuencial del usuario
    usuario_encontrado = buscar_usuario_secuencial(empleados_prueba, "juan123", "pass123")
    assert usuario_encontrado is not None
    assert usuario_encontrado[ID_EMPLEADO] == 1
    assert usuario_encontrado[NOMBRE] == "Juan"

def test_buscarClaveIncorrecta(empleados_prueba):
    #Busqueda de clave incorrecta
    usuario_encontrado = buscar_usuario_secuencial(empleados_prueba, "juan123", "pass_incorrecta")
    assert usuario_encontrado is None

def test_buscarUsuarioInexistente(empleados_prueba):
    #Busqueda de usuario inexistente
    usuario_encontrado = buscar_usuario_secuencial(empleados_prueba, "inexistente", "pass123")
    assert usuario_encontrado is None

def test_verificarExistencia(empleados_prueba):
    #Verificacion de existencia de usuario
    assert existe_usuario(empleados_prueba, "JUAN123") is True
    assert existe_usuario(empleados_prueba, "ana456") is True
    assert existe_usuario(empleados_prueba, "usuario_falso") is False

def test_obtenerSiguienteID(empleados_prueba):
    #Verificacion del siguiente ID disponible
    siguiente_id = obtener_id(empleados_prueba)
    assert siguiente_id == 3
