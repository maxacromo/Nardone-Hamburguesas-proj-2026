import pytest
from Clientes import Clientes as c

def test_busqueda_cliente_exit(monkeypatch):
    entradas = iter(["0", ""])
    monkeypatch.setattr("builtins.input", lambda *args: next(entradas))
    monkeypatch.setattr(c, "limpiar_pantalla", lambda: None)

    c.Busqueda_Cliente({}, [], ["yes","y","no","n"])

def test_destruir_cliente_exit(monkeypatch):
    entradas = iter(["0", ""])
    monkeypatch.setattr("builtins.input", lambda *args: next(entradas))
    monkeypatch.setattr(c, "limpiar_pantalla", lambda: None)

    resultado = c.Destruir_Cliente({}, ["yes","y","no","n"])
    assert resultado == {}

def test_update_cliente_exit(monkeypatch):
    entradas = iter(["0", ""])
    monkeypatch.setattr("builtins.input", lambda *args: next(entradas))
    monkeypatch.setattr(c, "limpiar_pantalla", lambda: None)

    resultado = c.Update_Cliente({}, ["yes","y","no","n"])
    assert resultado == {}
