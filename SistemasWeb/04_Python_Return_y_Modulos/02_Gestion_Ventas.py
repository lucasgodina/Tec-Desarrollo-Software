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
if __name__ == "__main__":
    while True:
        print("Seleccione una opción:")
        print("1. Agregar venta")
        print("2. Mostrar ventas")
        print("0. Salir del programa")
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            producto = input("Ingrese el nombre del producto vendido: ")
            precio = float(input("Ingrese el precio del producto vendido: "))
            agregar_venta(producto, precio)
        elif opcion == "2":
            mostrar_ventas()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 0.")
