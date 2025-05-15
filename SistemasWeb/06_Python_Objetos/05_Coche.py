"""
Crea una clase “Coche” con atributos como marca, modelo y año.
Implementa un método para encender el coche y otro para apagarlo (puedes simulae el encendido y apagado con una variable booleana).
"""


class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False

    def encender(self):
        self.encendido = True
        print(f"Coche encendido: {self.marca} {self.modelo} {self.año}")

    def apagar(self):
        self.encendido = False
        print(f"Coche apagado: {self.marca} {self.modelo} {self.año}")


# Crear objetos de la clase Coche
coche1 = Coche("Toyota", "Corolla", 2020)
coche2 = Coche("Honda", "Civic", 2019)
coche3 = Coche("Ford", "Focus", 2021)

# Mostrar información de cada coche
coche1.encender()
coche1.apagar()
coche2.encender()
coche2.apagar()
coche3.encender()
coche3.apagar()
