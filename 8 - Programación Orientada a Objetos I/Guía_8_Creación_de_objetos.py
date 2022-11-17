from typing import Optional


class Persona:
    """Clase que maneja datos de los vecinos"""

    def __init__(self, nombre: str, sexo: str, profesión: Optional[str] = None) -> None:
        self.nombre: str = nombre
        self.sexo: str = sexo
        self.profesión: Optional[str] = profesión

    def trabajo(self) -> str:
        if self.profesión:
            mensaje = f"{self.nombre} trabaja como {self.profesión}"
        else:
            mensaje = f"{self.nombre} no está trabajando"
        return mensaje


persona_1 = Persona("Esteban", "varón", "profesor")
persona_2 = Persona("Cintia", "mujer")

print(persona_1.nombre, persona_1.sexo, persona_1.profesión)
print(persona_2.nombre, persona_2.sexo, persona_2.profesión)


print(persona_1.trabajo())
print(persona_2.trabajo())
