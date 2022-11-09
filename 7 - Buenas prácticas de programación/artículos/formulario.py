from typing import Callable

from validación import validar
from . import validaciones


FORMULARIO: dict[str, dict[str, str | tuple[Callable, ...]]]
FORMULARIO = {
    "id": {
        "etiqueta": "Código: ",
        "acciones": (validar.entero_natural, validaciones.código)},
    "nombre": {
        "etiqueta": "Nombre: ",
        "acciones": (validar.cadena_no_vacía, validaciones.nombre)},
    "precio": {
        "etiqueta": "Precio: ",
        "acciones": (validar.real_positivo, validaciones.precio)},
    "cantidad": {
        "etiqueta": "Cantidad: ",
        "acciones": (validar.entero_natural, validaciones.cantidad)},
}
