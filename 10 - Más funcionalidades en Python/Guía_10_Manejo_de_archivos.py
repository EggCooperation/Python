import os

archivo = "mi_ruta.txt"
RUTA = os.getcwd()


def crear_archivo():
    if os.path.isfile(archivo):
        print(f"{archivo} ya existe")
    with open(archivo, "w") as f:
        print(f"Se creó el archivo {archivo}")


def escribir(*líneas):
    with open(archivo, "a") as f:
        for línea in líneas:
            f.write(str(línea) + "\n")


def leer():
    with open(archivo, "r") as f:
        datos = f.readlines()
        for índice, línea in enumerate(datos, start=1):
            print(índice, línea, end="")


def main():
    crear_archivo()

    escribir("Esta es mi ruta")
    escribir(RUTA)
    escribir(archivo)

    leer()

    escritura = ("Una línea", "Otra línea", 123)
    escribir(*escritura)


if __name__ == "__main__":
    main()
