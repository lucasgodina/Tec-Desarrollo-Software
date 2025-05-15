"""
Crea un sistema de gestión de una biblioteca utilizando clases en Python.
Debes implementar las siguientes clases:
1. “Libro”: Representa un libro con atributos como título, autor y número de
ejemplares disponibles.
2. “Usuario”: Representa a un usuario de la biblioteca con atributos como
nombre, número de identificación y lista de libros prestados.
3. “Biblioteca”: Representa la biblioteca en sí, con métodos para agregar
libros, prestar libros a usuarios, devolver libros y mostrar el inventario.
"""


class Libro:
    def __init__(self, titulo, autor, ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares = ejemplares

    def __str__(self):
        return f"{self.titulo} - Autor: {self.autor} - Ejemplares disponibles: {self.ejemplares}"


class Usuario:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} - ID: {self.identificacion} - Libros prestados: {len(self.libros_prestados)}"


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro agregado: {libro.titulo}")

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario registrado: {usuario.nombre}")

    def prestar_libro(self, libro, usuario):
        if libro in self.libros:
            self.libros.remove(libro)
            usuario.prestar_libro(libro)
        else:
            print(f"El libro '{libro.titulo}' no está disponible.")

    def devolver_libro(self, libro, usuario):
        if libro in usuario.libros_prestados:
            usuario.libros_prestados.remove(libro)
            self.libros.append(libro)
        else:
            print(f"El libro '{libro.titulo}' no fue prestado a {usuario.nombre}.")

    def mostrar_inventario(self):
        print("Inventario de la biblioteca:")
        for libro in self.libros:
            print(f" - {libro}")


# Ejemplo de uso
biblioteca = Biblioteca()
libro1 = Libro("Elantris", "Brandon Sanderson", 5)
libro2 = Libro("Mistborn: The Final Empire", "Brandon Sanderson", 3)
libro3 = Libro("Foundation", "Isaac Asimov", 2)
libro4 = Libro("Norwegian Wood", "Haruki Murakami", 4)
libro5 = Libro("Project Hail Mary", "Andy Weir", 6)
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)
biblioteca.agregar_libro(libro5)
usuario1 = Usuario("Juan Pérez", "123456")
usuario2 = Usuario("María López", "654321")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)
biblioteca.mostrar_inventario()
biblioteca.prestar_libro(libro1, usuario1)
biblioteca.mostrar_inventario()
biblioteca.devolver_libro(libro1, usuario1)
biblioteca.mostrar_inventario()
