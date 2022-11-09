def separar(numeros):
    """Crea dos listas ordenadas de números pares e impares"""
    numeros.sort()
    pares = []
    impares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares


def main():
    """
    - Pregunta al usuario cuántos números desea ingresar
    - El usuario ingresa los números
    - Se muestra dos listas de números ordenados de pares impares
    """
    bienvenida = "Ingresa números positivos y negativos"
    print(bienvenida)
    print("=" * len(bienvenida))
    lista = []
    cantidad = int(input("¿Cuántos números quieres ingresar? "))
    for n in range(cantidad):
        numero = int(input(f"{n + 1} número: "))
        lista.append(numero)
    
    pares, impares = separar(lista)
    print()
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")


main()