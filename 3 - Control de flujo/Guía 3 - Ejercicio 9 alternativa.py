número_1 = int(input("Ingrese el primer número: "))
número_2 = int(input("Ingrese el segundo número: "))

operaciones = (
    número_1 + número_2,  
    número_1 - número_2,  
    número_1 * número_2  
)

menú = ("Sumar", "Restar", "Multiplicar", "Salir")
mensaje = "Resultado de la operación:"

while True:
    for e, valor in enumerate(menú, start=1):
        print(e, "-", valor)
    opción = int(input("👉 "))
    índice = opción - 1 
    if índice > len(operaciones) or índice < 0:
        print("❌ Opción inválida")
        continue
    elif menú[índice] == "Salir":
        break
    else:
        print(mensaje, operaciones[índice])