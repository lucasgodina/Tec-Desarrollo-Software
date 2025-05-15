"""
Crea una clase "Pila" que represente una pila (stack) básica. Implementa
métodos para agregar elementos a la pila, quitar elementos y mostrar el
contenido actual.
"""


class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)
        print(f"Elemento apilado: {elemento}")

    def desapilar(self):
        if not self.esta_vacia():
            elemento = self.elementos.pop()
            print(f"Elemento desapilado: {elemento}")
            return elemento
        else:
            print("La pila está vacía.")

    def esta_vacia(self):
        return len(self.elementos) == 0

    def mostrar_contenido(self):
        if not self.esta_vacia():
            print("Contenido de la pila:")
            for elemento in reversed(self.elementos):
                print(elemento)
        else:
            print("La pila está vacía.")


# Ejemplo de uso
pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.mostrar_contenido()
pila.desapilar()
pila.mostrar_contenido()
