es_formulario_valido = True

while es_formulario_valido:
    usuario = input("Ingrese el usuario: ")
    if not len(usuario) > 5:
        print("Debe contener más de 5 caracteres")
        es_formulario_valido = False
        break
    if usuario[0].isdigit():
        print("El primer caracter no debe ser un número")
        es_formulario_valido = False
        break
    password = input("Ingrese el password: ")
    if not len(password) < 4:
        print("Debe contener menos de 4 caracteres")
        es_formulario_valido = False
        break
    repetir_password = input("Vuelva a ingresar el password: ")
    if not password == repetir_password:
        print("Los passwords no coinciden")
        es_formulario_valido = False
        break
    break
    
if es_formulario_valido:
    print("Formulario enviado")
else:
    print("Formulario inválido")
