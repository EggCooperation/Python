def validar_numero(entrada):
    """Valida si el parámetro recibido es un entero positivo o negativo
    Puede recibir, por ejemplo: 2022, -2022 o +2022
    """
    validar_1 = entrada.isdecimal()
    validar_2 = entrada[0] in ("-", "+")
    validar_3 = entrada[1:].isdecimal()
    if validar_1 or (validar_2 and validar_3):
        return True
    else:
        return False


def año_bisiesto(año):
    """Valida si el entero recibido es un año bisiesto o no.
    Puede recibir positivos o negativos"""
    validar_1 = año % 4 == 0
    validar_2 = not (año % 100 == 0)
    validar_3 = año % 400 == 0
    if validar_1 and (validar_2 or validar_3):
        return True
    else:
        return False

def main():
    while True:
        entrada = input("Ingrese un año (s: salir): ")
        if entrada == "s":
            break
        es_numero = validar_numero(entrada.strip())
        if not es_numero:
            continue
        año = int(entrada)
        es_año_bisiesto = año_bisiesto(año)
        if es_año_bisiesto:
            print(f"El año {año} sí es bisiesto.")
        else:
            print(f"No es bisiesto.")

main()