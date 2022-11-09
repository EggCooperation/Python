from .datos import artículos


def código(entrada: int) -> bool | int:
    if entrada > 1_000_000:
        print("❌ Código muy grande")
        return False
    elif entrada in artículos["artículo"].keys():
        print("❌ El código ya existe en otro artículo")
        return False
    else:
        return entrada


def nombre(entrada: str) -> bool | str:
    if not len(entrada) > 3 :
        print("❌ Nombre muy corto")
        return False
    elif not len(entrada) < 100:
        print("❌ Nombre muy largo")
        return False
    else:
        return entrada


def precio(entrada: float) -> bool | float:
    if entrada > 1_000_000_000:
        print("❌ Precio muy grande")
        return False
    else:
        return entrada


def cantidad(entrada: int) -> bool | int:
    if entrada > 1_000:
        print("❌ Cantidad muy grande")
        return False
    else:
        return entrada
