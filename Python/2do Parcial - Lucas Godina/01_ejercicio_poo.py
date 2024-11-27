# Clase Animal con atributos edad y especie
class Animal:
    def __init__(self, edad, especie):
        self.edad = edad
        self.especie = especie


# Creación de instancias perro y gato
perro = Animal(5, "Canino")
gato = Animal(3, "Felino")

print(f"El perro tiene {perro.edad} años y es de la especie {perro.especie}.")
print(f"El gato tiene {gato.edad} años y es de la especie {gato.especie}.")
