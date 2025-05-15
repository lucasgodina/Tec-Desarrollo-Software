"""
Crea una clase "Producto" con atributos como nombre, precio y cantidad en
stock. Luego, crea una clase "Tienda" que contenga una lista de productos
disponibles y métodos para agregar productos, mostrar el inventario y
realizar una compra.
"""


class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - Precio: {self.precio} - Cantidad: {self.cantidad}"


class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_inventario(self):
        for producto in self.productos:
            print(producto)

    def realizar_compra(self, nombre, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre:
                if producto.cantidad >= cantidad:
                    producto.cantidad -= cantidad
                    print(f"Compra realizada: {nombre} - Cantidad: {cantidad}")
                else:
                    print(f"Stock insuficiente para: {nombre}")
                return
        print(f"Producto no encontrado: {nombre}")


# Ejemplo de uso
tienda = Tienda()
producto1 = Producto("Laptop", 1000, 5)
producto2 = Producto("Teléfono", 500, 10)
producto3 = Producto("Tablet", 300, 0)
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)
tienda.mostrar_inventario()
tienda.realizar_compra("Laptop", 2)
tienda.mostrar_inventario()
tienda.realizar_compra("Tablet", 1)
tienda.mostrar_inventario()
