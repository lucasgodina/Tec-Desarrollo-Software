import json
from pathlib import Path

# Obtener el directorio del script en ejecución
SCRIPT_DIR = Path(__file__).parent
FILENAME = SCRIPT_DIR / "numero_favorito.json"


def obtener_numero_guardado():
    """Intenta leer el número favorito del archivo. Si no existe, devuelve None."""
    if FILENAME.exists():
        with open(FILENAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return None
    return None


def guardar_numero(numero):
    """Guarda el número favorito en un archivo."""
    with open(FILENAME, "w") as file:
        json.dump(numero, file)


def pedir_numero():
    """Solicita al usuario su número favorito."""
    while True:
        entrada = input("Introduce tu número favorito: ")
        if entrada.isdigit():
            return int(entrada)
        else:
            print("Por favor, introduce un número válido.")


def mostrar_o_guardar_numero():
    """Lógica principal del programa."""
    numero_guardado = obtener_numero_guardado()

    if numero_guardado is not None:
        print(f"Tu número favorito es: {numero_guardado}")
    else:
        numero_favorito = pedir_numero()
        guardar_numero(numero_favorito)
        print(f"Tu número favorito ha sido guardado: {numero_favorito}")


# Ejecutar la función principal
if __name__ == "__main__":
    mostrar_o_guardar_numero()
