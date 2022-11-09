from typing import Any

import artículos
import usuario


def main():
    TÍTULO: str = "NEGOCIO"
    OPCIONES: dict[str, dict[str, Any]]
    OPCIONES = {
        "1": {"etiqueta": "Artículos", "acción": artículos.menú.main},
        "2": {"etiqueta": "* Clientes"},
        "3": {"etiqueta": "* Ventas"},
        "x": {"etiqueta": "Salir", "acción": False},
    }
    usuario.menú.principal(TÍTULO, OPCIONES)


if __name__ == "__main__":
    main()
