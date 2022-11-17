from Guía_8_Composición import Persona, Cliente, Usuario


def test_Persona():
    persona = Persona(nombres="Esteban Horacio", apellidos="Acevedo Aberastain")
    assert persona.nombre_completo() == "Acevedo Aberastain, Esteban Horacio"


def test_Cliente():
    cliente = Cliente(nombres="Natalia Estefanía", apellidos="Algún Apellido", celular="1234")
    assert cliente.persona.nombres == "Natalia Estefanía"
    assert cliente.persona.apellidos == "Algún Apellido"
    assert cliente.celular == "1234"


def test_Usuario():
    cliente = Cliente(nombres="Natalia Estefanía", apellidos="Algún Apellido", celular="1234")
    usuario = Usuario(cliente)
    assert usuario.generar_contraseña() == "Natal34"
