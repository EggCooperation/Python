from typing import Self


class Producto:
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
            print()
            print(f"Código: {producto.código}")
            print(f"Nombre: {producto.nombre}")
            print(f"Precio: {producto.precio}")
            print(f"Stock: {producto.stock}")


if __name__ == "__main__":
    p1 = Producto(1, "Expreso", 400)
    p2 = Producto(2, "Cortado", 500)
    p3 = Producto(3, "Cappuchino", 600)

    p1.comprar(1)
    p1.comprar(1)
    p1.listar_productos()

    # lista_productos = [p1, p2, p3]

    # # p1.listar_productos()

    # p1.comprar(10)
    # p1.comprar(1)
    # p2.comprar(20)
    # p3.comprar(30)

    # p1.listar_productos()
    # print("************************")
    p1.vender(11)
    # p1.vender(9)
    p1.vender(1)
    # p2.vender(1)
    p1.listar_productos()
