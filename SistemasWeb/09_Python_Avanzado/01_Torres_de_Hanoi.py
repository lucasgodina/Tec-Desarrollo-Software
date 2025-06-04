"""
Tienes a tu disposición un conjunto de discos numerados del 1 al N y tres torres etiquetadas como A, B y C.
La torre A contiene inicialmente todos los discos apilados en orden descendente, desde el disco N en la parte inferior hasta el disco 1 en la parte superior.
Tu tarea es implementar una solución recursiva para mover todos los discos de la torre A a la torre C, siguiendo las reglas clásicas de las Torres de Hanoi:
1. Puedes mover un disco a una torre adyacente.
2. Solo puedes mover un disco a la cima de otra pila si esa pila está vacía o si el disco superior es más grande que el disco que estás colocando.
Debes definir una función llamada torres_de_hanoi(n, origen, destino, auxiliar) que, dado el número total de discos 'n' y las torres de origen, destino y auxiliar, imprima los pasos necesarios para lograr el movimiento de todos los discos desde la torre A a la torre C.

Entrada:
- N de discos
- N de torres
- Torres: origen, destino, auxiliar

Salida:
"Mover disco de la torre A a la torre D"
"Mover disco de la torre A a la torre B"
"""


def torres_de_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco de la torre {origen} a la torre {destino}")
    else:
        torres_de_hanoi(n - 1, origen, auxiliar, destino)
        print(f"Mover disco de la torre {origen} a la torre {destino}")
        torres_de_hanoi(n - 1, auxiliar, destino, origen)


# Ejemplo de uso
if __name__ == "__main__":
    N = 3  # Número de discos
    print("Ejemplo con 3 discos:")
    torres_de_hanoi(N, "A", "C", "B")  # A es origen, C es destino, B es auxiliar

    N = 4  # Otro ejemplo con 4 discos
    print("\nEjemplo con 4 discos:")
    torres_de_hanoi(N, "A", "C", "B")  # A es origen, C es destino, B es auxiliar
