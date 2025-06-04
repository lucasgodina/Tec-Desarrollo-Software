"""
Imagina que trabajas en una empresa de logística y tu tarea es desarrollar un sistema de gestión de inventario.
El inventario está representado como una lista de productos ordenados por sus códigos.
Cada producto se describe como un diccionario con las claves 'codigo' y 'cantidad'.
Tu objetivo es implementar una función recursiva que realice una búsqueda binaria en este inventario y devuelva la cantidad disponible para un producto específico, dado su código.

Entrada:
- Inventario de productos (json, dic, etc.)
- Código de producto buscado

Salida:
"Cantidad disponible para el producto con código X: Y"
"""


def buscar_producto(inventario, codigo):
    if not inventario:
        return 0

    medio = len(inventario) // 2
    if inventario[medio]["codigo"] == codigo:
        return inventario[medio]["cantidad"]
    elif inventario[medio]["codigo"] < codigo:
        return buscar_producto(inventario[medio + 1 :], codigo)
    else:
        return buscar_producto(inventario[:medio], codigo)


def imprimir_cantidad_disponible(inventario, codigo):
    cantidad = buscar_producto(inventario, codigo)
    if cantidad > 0:
        print(f"Cantidad disponible para el producto con código {codigo}: {cantidad}")
    else:
        print(f"Producto con código {codigo} no encontrado en el inventario.")


# Ejemplo de uso
if __name__ == "__main__":
    inventario = [
        {"codigo": 1, "cantidad": 10},
        {"codigo": 2, "cantidad": 5},
        {"codigo": 3, "cantidad": 0},
        {"codigo": 4, "cantidad": 8},
    ]
    imprimir_cantidad_disponible(inventario, 2)
    imprimir_cantidad_disponible(inventario, 5)
