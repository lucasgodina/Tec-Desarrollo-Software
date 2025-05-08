"""
VALIDACIÓN DE FORMULARIO
Crea un programa que valide un formulario de registro. Crea una función
llamada validar_formulario que reciba diferentes campos de un formulario
(nombre, correo electrónico y número de teléfono) y verifique si los valores
ingresados cumplen con los requisitos especificados, siendo estos:
1. Que el nombre tenga una longitud minima de 3 caracteres
2. Que el teléfono este conformado por dígitos y tenga una longitud de 9
caracteres
3. Que el email contenga un “@“ y un “.”
"""


def validar_formulario(nombre, correo, telefono):
    """
    Valida un formulario de registro.

    :param nombre: str, nombre del usuario
    :param correo: str, correo electrónico del usuario
    :param telefono: str, número de teléfono del usuario
    :return: bool, True si el formulario es válido, False en caso contrario
    """

    # Validar nombre
    if len(nombre) < 3:
        return False

    # Validar teléfono
    if not telefono.isdigit() or len(telefono) != 10:
        return False

    # Validar correo electrónico
    if "@" not in correo or "." not in correo:
        return False

    return True


# Ejemplo de uso
if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo electrónico: ")
    telefono = input("Ingrese su número de teléfono: ")

    if validar_formulario(nombre, correo, telefono):
        print("Formulario válido.")
    else:
        print("Formulario inválido.")
