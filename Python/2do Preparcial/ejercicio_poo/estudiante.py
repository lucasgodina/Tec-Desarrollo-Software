from persona import Persona


# Clase Estudiante que hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, matricula):
        super().__init__(nombre, edad, nacionalidad)
        self.matricula = matricula

    def mostrar_datos(self):
        print(
            f"Nombre: {self.nombre}\nEdad: {self.edad}\nNacionalidad: {self.nacionalidad}\nMatrícula: {self.matricula}"
        )

    # Sobreescritura del método saludar
    def saludar(self):
        print(f"Hola, soy {self.nombre} y soy estudiante")
