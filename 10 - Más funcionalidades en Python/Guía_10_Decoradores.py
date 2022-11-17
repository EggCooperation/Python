import datetime
import time


def dormir(func):
    def wrapper(*args, **kwargs):
        time.sleep(2)
        retorno = func(*args, **kwargs)
        return retorno
    return wrapper


class tiempo_log:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args):
        with open("registro.log", "a") as f:
            ahora = datetime.datetime.now()
            hora_str = ahora.strftime("%H:%M:%S.%f")
            f.write(hora_str + "\n")
        return self.func(*args)


@dormir
@tiempo_log
def mostrar():
    print(f"Ejecutando función")


def main():
    mostrar()
    mostrar()
    mostrar()


if __name__ == "__main__":
    main()
