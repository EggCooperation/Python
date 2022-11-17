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
        dni = input("Dni: ")
        apellidos = input("Apellidos: ")
        nombres = input("Nombres: ")
        fecha = input("Fecha de nacimiento (dd/mm/aaaa): ")
        nacimiento = datetime.strptime(fecha, "%d/%m/%Y").date()
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
    datos = asdict(cliente)
    with open("ejercicio_2.txt", "a") as archivo:
        for valor in datos.values():
            archivo.write(f"{valor}, ")
        archivo.write(datetime.now().strftime("creado: %A %d/%B/%Y %H:%M:%S\n"))


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
