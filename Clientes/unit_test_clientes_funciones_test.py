import pytest
import Clientes_Funciones as f

def test_search_client_id_found():
    clientes = {"123": ["Juan Perez", "jp@gmail.com", True]}
    assert f.Search_Client_ID("123", clientes) == ["Juan Perez", "jp@gmail.com", True]

def test_search_client_id_not_found():
    assert f.Search_Client_ID("999", {}) == "Not Found"

def test_gen_mail_unique():
    mails = []
    mail, usuario = f.Gen_Mail(mails, "Juan", "Perez")
    assert mail == "jperez@gmail.com"
    assert usuario.startswith("jperez")

def test_search_client_name_found():
    clientes = {"123": ["Juan Perez", "mail", True]}
    assert f.Search_Client_Name("Juan Perez", clientes, ["123"]) == "123"

def test_search_client_name_not_found():
    assert f.Search_Client_Name("Otro", {}, []) == "Not Found"

def test_gen_fullname(monkeypatch):
    entradas = iter(["Juan", "Perez", "y"])
    monkeypatch.setattr("builtins.input", lambda *args: next(entradas))
    monkeypatch.setattr(f, "limpiar_pantalla", lambda: None)

    assert f.Gen_FullName("", ["yes","y","no","n"]) == "Juan Perez"
