"""
Crea dos archivos, cats.txt y dogs.txt. Almacena al menos tres nombres de gatos en el primer archivo y tres nombres de perros en el segundo archivo. Escribe un programa que intente leer estos archivos e imprima el contenido de cada archivo en la pantalla. Envuelve tu código en un bloque try-except para capturar el error de FileNotFoundError, e imprime un mensaje amigable si falta algún archivo. Mueve uno de los archivos a una ubicación diferente en tu sistema y asegúrate de que el código en el bloque except se ejecute correctamente. Modifica tu bloque except para que falle en silencio si falta alguno de los archivos.
"""

from pathlib import Path

current_dir = Path(__file__).parent

try:
    cats_path = current_dir / "cats.txt"
    with cats_path.open("r") as cats_file:
        cats = cats_file.read()
        print("Cats:")
        print(cats)
except FileNotFoundError:
    pass

try:
    dogs_path = current_dir / "dogs.txt"
    with dogs_path.open("r") as dogs_file:
        dogs = dogs_file.read()
        print("Dogs:")
        print(dogs)
except FileNotFoundError:
    pass
