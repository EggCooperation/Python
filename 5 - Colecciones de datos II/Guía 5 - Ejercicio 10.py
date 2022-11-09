from pprint import pprint

articulos = {"artículo": {}}

while True:
    respuesta = input("¿Agrega un artículo? s/n: ").lower()
    if respuesta == "n":
        break
    elif respuesta == "s":
        codigo = int(input("Código: "))
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        datos = {"nombre": nombre, "precio": precio, "stock": stock}
        articulos["artículo"][codigo] = datos
        pprint(articulos)

compra = {"artículo": [], "total": 0}

while True:
    respuesta = input("¿Compra? s/n: ")
    if respuesta == "s":
        codigo = int(input("¿Qué desea? Ingresa el código: "))
        if codigo not in articulos["artículo"]:
            input("El código no existe")
            pprint(articulos)
        else:
            nombre = articulos["artículo"][codigo]["nombre"]
            precio = articulos["artículo"][codigo]["precio"]
            stock = articulos["artículo"][codigo]["stock"]
            if stock > 0:
                cantidad = int(input(f"¿Cuánto lleva? (máximo {stock}): "))
                articulos["artículo"][codigo]["stock"] -= cantidad
                compra["artículo"].append({"nombre": nombre, "precio": precio})
                compra["total"] += precio * cantidad
                print("SU COMPRA:")
                pprint(compra)
            else:
                input("No hay suficiente stock.")
                pprint(articulos)
    elif respuesta == "n":
        print("SU COMPRA:")
        pprint(compra)
        break
