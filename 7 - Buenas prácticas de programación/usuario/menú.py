from typing import Any

import validación


def mostrar(título: str, opciones: dict[str, dict[str, Any]]) -> None:
    print()
    print(f" {título} ".center(30, "*"))
    for descriptor, descripción in opciones.items():
        etiqueta = descripción["etiqueta"]
        print(f"{descriptor}. {etiqueta}")
    print()


def leer_opción(opciones: dict[str, dict[str, Any]]) -> str | None:
    opción = input(">>> Elige una opción: ")
    entrada_válida = validación.validar.cadena_no_vacía(opción)
    if entrada_válida:
        if opción in opciones.keys():
            return opción
        else:
            return None
    else:
        return None


def principal(título: str, opciones: dict[str, dict[str, Any]]) -> None:
    while True:
        mostrar(título, opciones)
        try:
            opción: str | None = leer_opción(opciones)
        except KeyboardInterrupt:
            break
        else:
            if opción:
                acción = opciones[opción].get("acción", None)
                if acción == None:
                    continue
                elif acción == False:
                    return None

                else:
                    acción()
            else:
                continue
