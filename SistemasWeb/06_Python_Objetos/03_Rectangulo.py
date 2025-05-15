"""
Crea una clase “Rectangulo” con atributos de longitud y ancho.
Implementa un método para calcular el área y el perímetro del rectángulo.
"""


class Rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def calcular_area(self):
        return self.longitud * self.ancho

    def calcular_perimetro(self):
        return 2 * (self.longitud + self.ancho)


# Crear objetos de la clase Rectangulo
rectangulo1 = Rectangulo(5, 3)
rectangulo2 = Rectangulo(7, 4)
rectangulo3 = Rectangulo(10, 2)

# Mostrar el área y el perímetro de cada rectángulo
print(
    f"Rectángulo 1 - Área: {rectangulo1.calcular_area()}, Perímetro: {rectangulo1.calcular_perimetro()}"
)
print(
    f"Rectángulo 2 - Área: {rectangulo2.calcular_area()}, Perímetro: {rectangulo2.calcular_perimetro()}"
)
print(
    f"Rectángulo 3 - Área: {rectangulo3.calcular_area()}, Perímetro: {rectangulo3.calcular_perimetro()}"
)
