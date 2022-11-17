from dataclasses import dataclass, field

@dataclass
class Rectángulo:
    _base: float
    _altura: float

    @staticmethod
    def validar_valor(valor):
        if not (isinstance(valor, (int, float)) and valor > 0):
            raise ValueError(f"{valor} el valor debe ser mayor a 0")
        return valor

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor: int|float):
        self.validar_valor(valor)
        self._base = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor: int | float):
        self.validar_valor(valor)
        self._altura = valor

    @property
    def área(self):
        return self._base * self._altura

    @property
    def diagonal(self):
        return (self._base**2 + self._altura**2) ** 0.5


@dataclass
class Cuadrado(Rectángulo):
    _lado: float
    _altura: float = field(init=False)
    _base: float = field(init=False)

    def __post_init__(self):
        self.validar_valor(self._lado)
        self._altura = self._lado
        self._base = self._lado

    @property
    def lado(self):
        return self._lado

    @lado.setter
    def lado(self, valor: int | float):
        self.validar_valor(valor)
        self._lado = valor
        self._base = valor
        self._altura = valor
   
    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor: int|float):
        self.lado = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor: int | float):
        self.lado = valor