"""
Encuentra o crea algunos textos que te gustaría analizar (puedes visitar Project Gutenberg (http://gutenberg.org/) o crear textos usando ChatGPT). Copia el texto sin formato desde tu navegador en un archivo de texto en tu computadora (o descarga los archivos). Averigua cuántas veces aparece una palabra o frase en el texto (puedes usar el método count()).
"""

import re
import pathlib


def contar_palabra_en_archivo(archivo, palabra):
    """
    Cuenta cuántas veces aparece una palabra en un archivo de texto.

    :param archivo: Ruta al archivo de texto.
    :param palabra: Palabra a buscar.
    :return: Número de ocurrencias de la palabra en el archivo.
    """
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
            # Usar re.escape para asegurar que la palabra se trate como una cadena literal
            return len(
                re.findall(r"\b" + re.escape(palabra) + r"\b", contenido, re.IGNORECASE)
            )
    except FileNotFoundError:
        print(f"El archivo {archivo} no fue encontrado.")
        return 0


if __name__ == "__main__":
    archivo = pathlib.Path(__file__).parent / "texto.txt"
    palabra = "python"
    ocurrencias = contar_palabra_en_archivo(archivo, palabra)
    print(
        f"La palabra '{palabra}' aparece {ocurrencias} veces en el archivo '{archivo}'."
    )
