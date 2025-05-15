"""
Crea una clase “Dado” que simule el lanzamiento de un dado de 6 caras.
Implementa un método para lanzar el dado y mostrar el resultado (quizás te convenga usar el modulo random).
"""

import random


class Dado:
    def __init__(self):
        self.caras = 6

    def lanzar(self):
        return random.randint(1, self.caras)


# Crear un objeto de la clase Dado
dado = Dado()

# Lanzar el dado varias veces y mostrar los resultados
for _ in range(10):
    resultado = dado.lanzar()
    print(f"Lanzamiento: {resultado}")
