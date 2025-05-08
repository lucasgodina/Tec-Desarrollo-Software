"""
Crea una función recursiva llamada suma_lista que calcule la suma de todos
los elementos de una lista de enteros. Puedes asumir que la lista no está
vacía.
"""


def suma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + suma_lista(lista[1:])


# Ejemplo de uso
print(suma_lista([20, 33, 17]))
