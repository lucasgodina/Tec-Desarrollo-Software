"""
Busca si tu fecha de nacimiento esta en los primeros 10000 digitos de pi (y en que posición. Puedes usar find()). Puedes usar el archivo pi_10000.txt
"""

from pathlib import Path

# Obtener la ruta del archivo en el mismo directorio que el script
script_dir = Path(__file__).parent
file_path = script_dir / "pi_10000.txt"

print(f"Los primeros 10000 dígitos de pi se han escrito en '{file_path}'.")

# Pedir al usuario su fecha de nacimiento en formato DDMMAA
fecha_nacimiento = input("Introduce tu fecha de nacimiento en formato DDMMAA: ")

# Leer el contenido del archivo 'pi_10000.txt'
try:
    with file_path.open("r") as file:
        contenido_pi = file.read()

    # Buscar la fecha de nacimiento en los dígitos de pi
    posicion = contenido_pi.find(fecha_nacimiento)

    if posicion != -1:
        print(
            f"Tu fecha de nacimiento aparece en los dígitos de pi en la posición {posicion}."
        )
    else:
        print("Tu fecha de nacimiento no aparece en los primeros 10000 dígitos de pi.")
except IOError as e:
    print(f"Error al leer el archivo: {e}")
