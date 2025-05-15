"""
Crea una clase llamada “Calculadora” con métodos para sumar, restar, multiplicar y dividir.
Crea objetos de esta clase y realiza algunas operaciones básicas.
"""


class Calculadora:
    def __init__(self):
        pass

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        return a / b


# Crear un objeto de la clase Calculadora
calculadora = Calculadora()

# Realizar algunas operaciones básicas
print(calculadora.sumar(5, 3))
print(calculadora.restar(5, 3))
print(calculadora.multiplicar(5, 3))
print(calculadora.dividir(5, 3))
