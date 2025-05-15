"""
Define una clase Persona con atributos como nombre, edad y profesión.
Luego, crea varios objetos de esta clase y muestra su información.
"""


class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Profesión: {self.profesion}")


# Crear objetos de la clase Persona
persona1 = Persona("Lucas", 30, "Project Manager")
persona2 = Persona("Jazmín", 22, "Backend Developer")
persona3 = Persona("Jorgelina", 40, "Designer")

# Mostrar información de cada persona
persona1.mostrar_informacion()
persona2.mostrar_informacion()
persona3.mostrar_informacion()
