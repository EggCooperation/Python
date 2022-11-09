usuario = input("Ingrese el usuario: ")
password = input("Ingrese el password: ")
repetir_password = input("Vuelva a ingresar el password: ")

validacion_1 = len(usuario) > 5
validacion_2 = not usuario[0].isdigit()
validacion_3 = len(password) < 4
validacion_4 = password == repetir_password

es_formulario_valido = True

if not validacion_1:
    print("La longitud de usuario debe ser mayor a 5")
    es_formulario_valido = False

if not validacion_2:
    print("El primer caracter de usuario NO debe ser un dígito")
    es_formulario_valido = False

if not validacion_3:
    print("Longitud de password debe ser menor a 4")

if not validacion_4:
    print("El password no es igual")
    es_formulario_valido = False

if es_formulario_valido:
    print("Formulario enviado")
else:
    print("Formulario inválido")
