"""
Imagina que estás desarrollando un sistema de reservas de vuelos para una
aerolínea. Crea un sistema de clases que permita a los usuarios realizar
reservas de vuelos. Aquí tienes una posible estructura:
- Clase base: `Vuelo`
- Atributos: número de vuelo, origen, destino, capacidad máxima, lista de
pasajeros
- Métodos: agregar pasajero, verificar disponibilidad de asientos
- Clase derivada: `VueloEspecial` (hereda de `Vuelo`)
- Atributos adicionales: motivo del vuelo especial (por ejemplo, vacaciones,
trabajo)
Resuelve el problema creando instancias de estas clases y realizando
reservas para diferentes vuelos y tipos de vuelos especiales.
"""

import Vuelo, VueloEspecial


def main():
    # Crear instancias de vuelos
    vuelo1 = Vuelo.Vuelo("AA123", "Nueva York", "Los Ángeles", 2)
    vuelo2 = VueloEspecial.VueloEspecial("BB456", "Miami", "Las Vegas", 3, "Urgente")

    vuelo1.agregar_pasajero("Juan Pérez")
    vuelo1.agregar_pasajero("María López")
    vuelo1.agregar_pasajero(
        "Carlos García"
    )  # Este no se agregará porque el vuelo está lleno

    vuelo2.agregar_pasajero("Ana Torres")
    vuelo2.agregar_pasajero("Luis Fernández")

    vuelo1.verificar_disponibilidad()
    vuelo2.verificar_disponibilidad()
    print(f"Motivo del vuelo especial: {vuelo2.motivo}")


if __name__ == "__main__":
    main()
