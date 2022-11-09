from typing import Any


def a_int(entrada: Any) -> bool | int:
    """
    Valida la entrada para convertir a un int.
    Devuelve int si es válida, si no False.
    """
    salida: int
    try:
        if "." in str(entrada):
            raise Exception
        salida = int(entrada)
    except Exception:
        return False
    else:
        return salida


def a_float(entrada: Any) -> bool | float:
    """
    Valida la entrada para convertir a un float.
    Devuelve float si es válida, si no False.
    """
    salida: float
    try:
        salida = float(entrada)
    except Exception:
        return False
    else:
        return salida


def a_str(entrada: Any) -> bool | str:
    """
    Valida la entrada para convertir a un str.
    Solo acepta int, float y str.
    Devuelve str si es válida, si no False.
    """
    salida: str
    if not type(entrada) in (int, float, str):
        return False
    else:
        salida = str(entrada)
        return salida
