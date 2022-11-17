from typing import Self


class Administrador:
    password: str = "admin"

    def verificar_administrador(self) -> bool:      
        entrada = input("Ingrese la constraseña: ") 
        if entrada == Administrador.password:
            print("👌 correcto")
            return True
        else:
            print("😔 incorrecto")
            return False


class Producto(Administrador):
    impuestos: float = 21.0
    lista_productos: list[Self] = []

    def __init__(self, código: int, nombre: str, precio: float) -> None:
        self.código: int = código
        self.nombre: str = nombre
        self.precio: float = self.precio_final(precio)
        self.stock: int = 0

    def precio_final(self, precio: float) -> float:
        return (precio * self.impuestos / 100) + precio

    def comprar(self, cantidad: int) -> None:
        print(f"Intentando comprar: {self.nombre}. Se requiere ser administrador") # Esto es lo nuevo
        if not self.verificar_administrador():  # Esto es lo nuevo
            print("❌ No se pudo comprar")  # Esto es lo nuevo
            return  # Esto es lo nuevo

        if self in Producto.lista_productos:
            if cantidad > 0:
                self.stock += cantidad
                print(
                    f"✅ Comprado: {self.nombre} (cantidad: {cantidad}, stock: {self.stock})")
            else:
                print(f"❌ La cantidad a comprar debe ser superior a 0.")
        else:
            if cantidad > 0:
                self.stock += cantidad
                Producto.lista_productos.append(self)
                print(
                    f"✅ Nuevo producto: {self.nombre} (cantidad: {cantidad})")
            else:
                print(f"❌ La cantidad a comprar debe ser superior a 0.")

    def vender(self, cantidad: int) -> None:
        if self in Producto.lista_productos:
            if cantidad < 1:
                print(f"❌ La cantidad a vender debe ser superior a 1.")
            elif self.stock > cantidad:
                self.stock -= cantidad
                print(
                    f"✅ Vendido: {self.nombre} (cantidad: {cantidad}, stock: {self.stock})")
            elif self.stock == cantidad:
                print(f"✅ Vendido: {self.nombre} (cantidad: {cantidad})")
                print(f"🤔 No queda más {self.nombre}")
                Producto.lista_productos.remove(self)
            else:
                print(
                    f"❌ {self.nombre}: Quiere vender {cantidad}, pero hay {self.stock} en total.")
        else:
            print(f"❌ {self.nombre}: no existe. No se hizo la venta.")

    def listar_productos(self) -> None:
        for producto in Producto.lista_productos:
            tipo = producto.__class__.__name__
            print()
            print(f"Código: {producto.código} - {tipo}")
            print(f"Nombre: {producto.nombre}")
            print(f"Precio: {producto.precio}")
            print(f"Stock: {producto.stock}")
            if isinstance(producto, Café):
                print(f"Descripción: {producto.descripción}")
                print(f"Proveedor: {producto.proveedor}")
            if isinstance(producto, Libro):
                print(f"Autor: {producto.autor}")
                print(f"ISBN: {producto.isbn}")


class Libro(Producto):
    def __init__(self, código: int, nombre: str, precio: float, autor: str, isbn: str) -> None:
        super().__init__(código, nombre, precio)
        self.autor: str = autor
        self.isbn: str = isbn


class Café(Producto):
    def __init__(self, código: int, nombre: str, precio: float, descripción: str, proveedor: str) -> None:
        super().__init__(código, nombre, precio)
        self.descripción: str = descripción
        self.proveedor: str = proveedor

if __name__ == "__main__":
    café = Café(1, "Expreso", 400.0, "café solo", "Gran Café")
    libro = Libro(2, "El Principito", 1500, "Antoine de Saint-Exupéry", "9788446033677")
    producto = Producto(34, "Agua mineral", 100)

    café.comprar(3)
    libro.comprar(10)
    producto.comprar(1)
    café.comprar(3)
    producto.listar_productos()
