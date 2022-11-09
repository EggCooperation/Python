nombre = input("Nombre: ")
edad = int(input("Edad: "))

validacion_1 = nombre != "****"
validacion_2 = edad > 12 and edad < 18
validacion_3 = len(nombre) >= 3 and len(nombre) < 10

validar = validacion_1 and validacion_2 and validacion_3
print(validar)