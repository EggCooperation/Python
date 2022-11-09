numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))

while True:
    print("1. Sumar los números")
    print("2. Restar los números")
    print("3. Multiplicar los números")
    print("4. Salir")
    opción = input("👉 ")
    if opción == "1":
        print(f"{numero_1} + {numero_2} = {numero_1 + numero_2}")
    elif opción == "2":
        print(f"{numero_1} - {numero_2} = {numero_1 - numero_2}")
    elif opción == "3":
        print(f"{numero_1} * {numero_2} = {numero_1 * numero_2}")
    elif opción == "4":
        break
    else:
        print("⛔ Opción inválida")
        continue
    