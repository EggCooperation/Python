class Persona:
    def __init__(self, nombres: str, apellidos: str):
        self.nombres: str = nombres
        self.apellidos: str = apellidos

    def nombre_completo(self) -> str:
        return f"{self.apellidos}, {self.nombres}"


class Cliente(Persona):
    def __init__(self, nombres: str, apellidos: str, celular: str):
        super().__init__(nombres, apellidos)
        self.celular: str = celular


class Usuario(Cliente):
    def __init__(self, nombres: str, apellidos: str, celular: str):
        super().__init__(nombres, apellidos, celular)
        self.contraseña: str = self.generar_contraseña()

    def generar_contraseña(self) -> str:
        return f"{self.nombres[:5]}{self.celular[-2:]}"


persona = Persona(nombres="Guillermo Guillermino",
                  apellidos="González Páez")

cliente = Cliente(nombres="Guillerma Guillermina",
                  apellidos="Romana",
                  celular="123456789")

usuario = Usuario(nombres="Adrían", apellidos="Rodríguez", celular="43232")

print(persona.nombre_completo())
print(cliente.nombre_completo(), cliente.celular)
print(f"{usuario.nombre_completo()} {usuario.celular=} {usuario.contraseña=}")
