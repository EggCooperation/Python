import json
import os
from dataclasses import asdict, dataclass
from datetime import date, datetime


@dataclass
class Cliente:
    dni: str
    apellidos: str
    nombres: str
    nacimiento: date


def cliente_crear() -> Cliente | None:
    try:
        dni = input("DNI: ")
        apellidos = input("Apellidos: ")
        nombres = input("Nombres: ")
        fecha = input("Fecha de nacimiento (dd/mm/aaaa): ")
        nacimiento: date = datetime.strptime(fecha, "%d/%m/%Y").date()
        if nacimiento > datetime.now().date():
            raise Exception(
                "El nacimiento no puede ser mayor a la fecha actual")
    except Exception as e:
        print("ERROR:", e)
        return None
    else:
        cliente = Cliente(dni, apellidos, nombres, nacimiento)
        return cliente


def cliente_guardar(cliente: Cliente):
    lista_clientes: list[dict[str, str]] = []

    if os.path.isfile("ejercicio_3.json"):
        with open("ejercicio_3.json", "r") as f:
            try:
                lista_clientes = json.load(f)
            except ValueError as e:
                print(e)

    with open("ejercicio_3.json", "w") as f:
        datos = asdict(cliente)
        lista_clientes.append(datos)
        json.dump(lista_clientes, f, indent=4, default=str)


def main():
    import locale
    locale.setlocale(locale.LC_ALL, "")
    for número in range(1, 4):
        print("CLIENTE", número)
        nuevo_cliente = cliente_crear()
        if nuevo_cliente:
            cliente_guardar(nuevo_cliente)


if __name__ == "__main__":
    main()
