class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")

    def set_edad(self, edad):
        self.edad = edad


lucas = Persona("Lucas", 30, "Argentina")
sebastian = Persona("Sebastian", 40, "Uruguay")

lucas.saludar()
