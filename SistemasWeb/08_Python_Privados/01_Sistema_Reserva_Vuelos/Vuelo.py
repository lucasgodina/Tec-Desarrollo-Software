class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, capacidad_maxima):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.capacidad_maxima = capacidad_maxima
        self.lista_pasajeros = []

    def agregar_pasajero(self, pasajero):
        if len(self.lista_pasajeros) < self.capacidad_maxima:
            self.lista_pasajeros.append(pasajero)
            return print(f"Pasajero {pasajero} agregado al vuelo {self.numero_vuelo}.")
        else:
            return print(
                f"No se pudo agregar al pasajero {pasajero}. El vuelo está lleno."
            )

    def verificar_disponibilidad(self):
        if len(self.lista_pasajeros) < self.capacidad_maxima:
            print(f"Hay disponibilidad en el vuelo {self.numero_vuelo}.")
        else:
            print(f"No hay disponibilidad en el vuelo {self.numero_vuelo}.")
