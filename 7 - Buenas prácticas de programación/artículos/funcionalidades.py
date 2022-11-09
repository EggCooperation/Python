from pprint import pprint

import usuario

from .datos import artículos
from .formulario import FORMULARIO


def ver() -> None:
    if artículos["artículo"]:
        pprint(artículos, sort_dicts=False)
    else:
        print("❌ No hay artículos registrados")
    return


def agregar() -> None:
    formulario_ingresado = usuario.entrada_datos.entrada(FORMULARIO)
    if formulario_ingresado:
        artículos["artículo"].update(formulario_ingresado)
        print("✅ Artículo agregado")
    return

