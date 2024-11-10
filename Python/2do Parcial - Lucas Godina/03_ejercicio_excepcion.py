# Definición de la excepción EdadInvalidaError
class EdadInvalidaError(Exception):
    def __init__(self, edad, message="La edad no puede ser negativa"):
        self.edad = edad
        self.message = message
        super().__init__(self.message)


# Función que verifica si la edad es válida
def verificar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError(edad)
    return True


# Try-except que maneja la excepción EdadInvalidaError y ValueError
try:
    edad = int(input("Introduce tu edad: "))
    verificar_edad(edad)
    print("Edad válida.")
except EdadInvalidaError as e:
    print(f"Error: {e.message}. Edad introducida: {e.edad}")
except ValueError:
    print("Error: Debes ingresar un número entero.")
