class Persona:
    """ Datos de una persona"""

    def __init__(self, nombres: str, apellidos: str):
        self.nombres: str = nombres
        self.apellidos: str = apellidos

    def nombre_completo(self) -> str:
        """ Devuelve primero los apellidos y luego los nombres"""
        return f"{self.apellidos}, {self.nombres}"


class Cliente:
    """ Datos de un cliente"""

    def __init__(self, nombres: str, apellidos: str, celular: str):
        self.persona = Persona(nombres, apellidos)  # Composición
        self.celular: str = celular


class Usuario:
    """ Datos de un usuario """

    def __init__(self, cliente: Cliente):
        self.cliente: Cliente = cliente  # Agregación
        self.contraseña: str = self.generar_contraseña()

    def generar_contraseña(self) -> str:
        """
        Genera una contraseña con los 5 primeros caracteres de 'cliente.nombres'
        y con  los últimos 2 caracteres de 'cliente.celular'
        """
        return f"{self.cliente.persona.nombres[:5]}{self.cliente.celular[-2:]}"


def main():
    persona = Persona(nombres="Esteban Horacio", apellidos="Acevedo Aberastain")
    print(persona.nombre_completo())

    cliente = Cliente("Natalia Estefanía", "Algún Apellido", "1234")
    print(cliente.persona.nombre_completo(), cliente.celular)

    usuario = Usuario(cliente)
    print(usuario.contraseña)


main()
