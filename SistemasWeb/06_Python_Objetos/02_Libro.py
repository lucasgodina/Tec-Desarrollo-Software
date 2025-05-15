"""
Crea una clase “Libro” con atributos como título, autor y año de publicación.
Luego, crea varios objetos Libro y muestra su información.
"""


class Libro:
    def __init__(self, titulo, autor, year_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.year_publicacion = year_publicacion

    def mostrar_informacion(self):
        print(
            f"Título: {self.titulo}, Autor: {self.autor}, Año de publicación: {self.year_publicacion}"
        )


# Crear objetos de la clase Libro
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
libro3 = Libro("1984", "George Orwell", 1949)

# Mostrar información de cada libro
libro1.mostrar_informacion()
libro2.mostrar_informacion()
libro3.mostrar_informacion()
