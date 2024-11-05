<<<<<<< HEAD
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.__edad = edad  # Cambiar a __edad para indicar que es privado
        self.nacionalidad = nacionalidad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")

    @property  # Decorador para obtener el valor de la edad, "getter" en Java
    def edad(self):
        return self.__edad

    @edad.setter  # Decorador para modificar el valor de la edad, "setter" en Java
    def set_edad(self, edad):
        try:
            if edad >= 0:
                self.__edad = edad
            else:
                print("La edad no puede ser negativa")
        except ValueError:
            print("La edad debe ser un número entero")
=======
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.__edad = edad  # Cambiar a __edad para indicar que es privado
        self.nacionalidad = nacionalidad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")

    @property  # Decorador para obtener el valor de la edad, "getter" en Java
    def edad(self):
        return self.__edad

    @edad.setter  # Decorador para modificar el valor de la edad, "setter" en Java
    def set_edad(self, edad):
        try:
            if edad >= 0:
                self.__edad = edad
            else:
                print("La edad no puede ser negativa")
        except ValueError:
            print("La edad debe ser un número entero")
>>>>>>> 4a23642f34a0ab7df19d93af58be603e9bb86e08
