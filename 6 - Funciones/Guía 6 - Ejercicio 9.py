def tiempo_convertir(horas, minutos, segundos):
    """Convierte cualquier número al formato de tiempo estándar."""
    while segundos >= 60:
        minutos += segundos // 60
        segundos %= 60
    while minutos >= 60:
        horas += minutos // 60
        minutos %= 60
    dias = 0
    while horas >= 24:
        dias += horas // 24
        horas %= 24
    return (dias, horas, minutos, segundos)


def tiempo_formatear(dias, horas, minutos, segundos):
    """Representa en cadena: días, horas, minutos y segundos"""
    if dias == 1:
        tiempo = f"{dias} día, {horas:02}h {minutos:02}m {segundos:02}s"
    elif dias > 1:
        tiempo = f"{dias} días, {horas:02}h {minutos:02}m {segundos:02}s"
    else:
        tiempo = f"{horas:02}h {minutos:02}m {segundos:02}s"
    return tiempo


def numeros_validar(*args):
    """Valida si todos los caracteres de una cadena son números"""
    for arg in args:
        if not arg.isdigit():
            return False
    return True


def main():
    """
    - Pregunta al usuario por horas, minutos y segundos.
    - Valida si los datos son números: numeros_validar.
    - Convierte los datos en tiempo: tiempo_convertir.
    - Muestra el tiempo en una cadena legible: tiempo_formatear.
    """

    while True:
        print("Conversor de tiempo (sale si no introduce números)")
        horas = input("Horas: ")
        minutos = input("Minutos: ")
        segundos = input("Segundos: ")
        validacion = numeros_validar(horas, minutos, segundos)
        if not validacion:
            break
        else:
            horas = int(horas)
            minutos = int(minutos)
            segundos = int(segundos)
            tiempo_convertido = tiempo_convertir(horas, minutos, segundos)
            mensaje = tiempo_formatear(*tiempo_convertido)
            print(mensaje)

main()