from estudiante import Estudiante
from persona import Persona


def main():
    lucas = Estudiante("Lucas", 30, "Argentina", 123456)
    eduardo = Estudiante("Eduardo", 25, "Venezuela", 654321)
    jazmin = Persona("Jazmín", 21, "Argentina")

    # Demostración de polimorfismo, sobreescritura del método saludar
    lucas.saludar()
    eduardo.saludar()
    jazmin.saludar()

    # No se puede acceder a la edad de Lucas directamente
    lucas.__edad = 31
    print(f"Lucas cumplió años, ahora tiene {lucas.edad} años")

    # Se debe utilizar el método set_edad para modificar la edad
    lucas.set_edad = 31
    print(f"Lucas cumplió años, ahora tiene {lucas.edad} años")


if __name__ == "__main__":
    main()
