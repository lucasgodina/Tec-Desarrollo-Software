"""
CONTRASENA SEGURA
Crea un script que solicite una contraseña, analice si es segura y si no lo es
sugiera una nueva contraseña. Para ello puedes crear un script validador.py
que contenga una funcion validar_contrasena que reciba una cadena y
verifique si cumple con los requisitos mínimos de una contraseña segura
(por ejemplo, longitud mínima, presencia de letras mayúsculas, letras
minúsculas, números y caracteres especiales). La función debe devolver un
valor booleano que indique si la contraseña es válida o no. Por otro lado
puedes crear otro script creador.py con una función llamada
generar_contrasena que genere contraseñas seguras de forma aleatoria. La
función debe permitir especificar la longitud de la contraseña y qué tipos de
caracteres deben incluirse (por ejemplo, letras mayúsculas, letras
minúsculas, números y caracteres especiales).
(Para el generador de contraseñas puedes probar a usar los modulos
random y string)
"""

import random
import string
from validador import validar_contrasena


def generar_contrasena(
    longitud=12, mayusculas=True, minusculas=True, numeros=True, especiales=True
):
    """
    Genera una contraseña segura aleatoria.

    :param longitud: int, longitud de la contraseña (por defecto 12)
    :param mayusculas: bool, incluir letras mayúsculas (por defecto True)
    :param minusculas: bool, incluir letras minúsculas (por defecto True)
    :param numeros: bool, incluir números (por defecto True)
    :param especiales: bool, incluir caracteres especiales (por defecto True)
    :return: str, contraseña generada
    """
    caracteres = ""
    if mayusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if especiales:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Al menos un tipo de carácter debe ser seleccionado.")

    contrasena = "".join(random.choice(caracteres) for _ in range(longitud))

    return contrasena
