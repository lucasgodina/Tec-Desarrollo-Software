"""
Imagina que eres parte de un equipo de desarrollo de IA que se encarga de crear un sistema para que un robot resuelva laberintos. El laberinto está representado por una matriz, donde ciertos valores indican caminos permitidos (0), paredes (1), y la salida (9). Tu tarea es implementar una función recursiva que encuentra la ruta más corta para que el robot salga del laberinto.
Toma en cuenta los siguientes puntos:
1. La matriz representa el laberinto, donde los valores son:
- 0: Camino permitido
- 1: Pared
- 9: Salida
2. Debes implementar la función 'resolver_laberinto' que utiliza recursividad para encontrrar la ruta más corta desde una posición inicial hasta la salida.
3. La función debe devolver una lista de coordenadas que representan la ruta desde la posición inicial hasta la salida.
4. Puedes usar una lista de movimientos posibles: arriba (-1, 0), abajo (1, 0), izquierda (0, -1), derecha (0, 1).

Entrada:
- Laberinto (matriz)
- Indice de inicio (fila)
- Indice de inicio (columna)

Salida:
Camino para salir del laberinto: (1,1), (1,2)), ...
"""


def resolver_laberinto(laberinto, fila, columna, camino=None):
    if camino is None:
        camino = []

    # Verificar límites y condiciones de salida
    if (
        fila < 0
        or fila >= len(laberinto)
        or columna < 0
        or columna >= len(laberinto[0])
    ):
        return None
    if laberinto[fila][columna] == 1:
        return None
    if laberinto[fila][columna] == 9:
        camino.append((fila, columna))
        return camino

    # Marcar el camino actual
    laberinto[fila][columna] = 1
    camino.append((fila, columna))

    # Intentar movimientos en todas las direcciones
    for movimiento in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nueva_fila = fila + movimiento[0]
        nueva_columna = columna + movimiento[1]
        resultado = resolver_laberinto(
            laberinto, nueva_fila, nueva_columna, camino.copy()
        )
        if resultado is not None:
            return resultado

    # Desmarcar el camino si no se encontró solución
    laberinto[fila][columna] = 0
    camino.pop()
    return None


# Ejemplo de uso
if __name__ == "__main__":
    laberinto = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 9],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 1, 1, 1, 0],
    ]
    fila_inicio = 0
    columna_inicio = 0

    camino = resolver_laberinto(laberinto, fila_inicio, columna_inicio)
    if camino:
        print("Camino para salir del laberinto:", camino)
    else:
        print("No se encontró un camino hacia la salida.")
