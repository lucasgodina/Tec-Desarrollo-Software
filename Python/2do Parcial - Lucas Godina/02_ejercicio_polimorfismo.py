class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"Hola, soy {self.nombre}."


# Clases Estudiante y Profesor que heredan de Persona y sobreesciben el método saludar
class Estudiante(Persona):
    def saludar(self):
        return f"Hola, soy {self.nombre} y soy estudiante."


class Profesor(Persona):
    def saludar(self):
        return f"Hola, soy {self.nombre} y soy profesor."


# Función que recibe una persona y la presenta
def presentar_persona(persona):
    print(persona.saludar())


# Creación de instancias estudiante y profesor
estudiante = Estudiante("Lucas")
profesor = Profesor("Sergio")

presentar_persona(estudiante)
presentar_persona(profesor)
