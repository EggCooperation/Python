mis_numeros = []

while True:
    numero = input("Número: ")
    if numero:
        numero = int(numero)
        mis_numeros.append((numero,))
    else:
        break
    
for indice in range(len(mis_numeros)):
    print(*mis_numeros[indice])

for numero in mis_numeros:
    print(*numero)
        