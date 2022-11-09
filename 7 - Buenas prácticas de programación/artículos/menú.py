from typing import Any

import usuario

from . import funcionalidades


def main():
    TÍTULO: str = "ARTÍCULOS"
    OPCIONES: dict[str, dict[str, Any]]
    OPCIONES = {
        "1": {"etiqueta": "Ver artículos", "acción": funcionalidades.ver},
        "2": {"etiqueta": "Agregar un artículo", "acción": funcionalidades.agregar},
        "3": {"etiqueta": "* Modificar un artículo"},
        "4": {"etiqueta": "* Eliminar un artículo"},
        "x": {"etiqueta": "Salir", "acción": False},
    }
    usuario.menú.principal(TÍTULO, OPCIONES)
