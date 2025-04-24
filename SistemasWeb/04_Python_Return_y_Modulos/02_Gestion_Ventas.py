"""
GESTIÓN DE VENTAS
Crea un programa que permita gestionar las ventas de una tienda. Utiliza una
estructura de datos adecuada para almacenar la información de las ventas
(por ejemplo, una lista de diccionarios). Implementa dos funciones, una para
agregar el producto vendido con su precio y otro para mostrar las ventas de
productos con sus respectivos precios.
(La base de datos puede tener la forma [{“Producto”: producto1, “Precio”:
precio1}, {“Producto”: producto2, “Precio”: precio2}...])
"""

ventas = []  # Lista de diccionarios para almacenar las ventas


def agregar_venta(producto, precio):
    """
    Agrega una venta a la lista de ventas.

    :param producto: str, nombre del producto vendido
    :param precio: float, precio del producto vendido
    """
    venta = {"Producto": producto, "Precio": precio}
    ventas.append(venta)
    print(f"Venta agregada: {venta}")


def mostrar_ventas():
    """
    Muestra todas las ventas registradas.
    """
    if not ventas:
        print("No hay ventas registradas.")
        return

    print("Ventas registradas:")
    for venta in ventas:
        print(f"Producto: {venta['Producto']}, Precio: {venta['Precio']}")


# Ejemplo de uso
agregar_venta("Laptop", 1200.50)
agregar_venta("Teléfono", 800.75)
agregar_venta("Tablet", 300.00)

mostrar_ventas()
