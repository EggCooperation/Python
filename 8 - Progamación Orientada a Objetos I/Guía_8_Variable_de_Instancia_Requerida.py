from typing import Optional


class Persona:
    """Clase que maneja datos de los vecinos"""

    vecindario: str = "Buenos Vecinos"

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

print(persona_1.vecindario)
print(persona_2.vecindario)
print(Persona.vecindario)

Persona.vecindario = "Nuevo Barrio"
print(persona_1.vecindario)
print(persona_2.vecindario)
print(Persona.vecindario)

persona_1.vecindario = "La Costa"
print(persona_1.vecindario)
print(persona_2.vecindario)
print(Persona.vecindario)


print(persona_1.__dict__)
print(persona_2.__dict__)
