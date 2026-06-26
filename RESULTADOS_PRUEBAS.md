# Resultados de Pruebas Unitarias

**Fecha:** 2026-06-26 · **Comando:** `python -m pytest tests/ Clientes/ -v`

## Resultado: ✅ 14/14 pasaron (0 fallos)

| Módulo | Tests | Estado |
|---|---|---|
| `tests/test_empleados.py` | 5 | ✅ |
| `Clientes/unit_test_clientes_funciones_test.py` | 6 | ✅ |
| `Clientes/unit_test_clientes_test.py` | 3 | ✅ |

## Nota

Los 3 tests de `unit_test_clientes_test.py` fallaban por un conflicto de imports
(la carpeta `Clientes/` y el archivo `Clientes.py` con el mismo nombre). Se
corrigió usando imports de paquete en los tests (`from Clientes import Clientes`).
