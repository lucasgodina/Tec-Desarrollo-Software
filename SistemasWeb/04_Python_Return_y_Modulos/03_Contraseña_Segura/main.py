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

from validador import validar_contrasena
from creador import generar_contrasena


def main():
    while True:
        # Seleccionar que tipo de función ejecutar
        print("Seleccione una opción:")
        print("1. Validar contraseña")
        print("2. Generar contraseña segura")
        print("0. Salir del programa")
        opcion = input("Ingrese el número de la opción deseada: ")
        # Validar la opción seleccionada
        if opcion == "1":
            contrasena = input("Ingrese la contraseña a validar: ")
            if validar_contrasena(contrasena):
                print("La contraseña es segura.")
            else:
                print("La contraseña no es segura.")
        # Generar una nueva contraseña
        if opcion == "2":
            print("Generamos una contraseña segura")
            longitud = int(input("Ingrese la longitud de la contraseña: "))
            mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").lower() == "s"
            minusculas = input("¿Incluir letras minúsculas? (s/n): ").lower() == "s"
            numeros = input("¿Incluir números? (s/n): ").lower() == "s"
            especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == "s"
            contrasena = generar_contrasena(
                longitud, mayusculas, minusculas, numeros, especiales
            )
            print(f"Contraseña generada: {contrasena}")
        # Salir del programa
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        # Opción no válida
        else:
            print(
                "Opción no válida. Por favor, seleccione 1 o 2. Para salir, seleccione 0."
            )


# Ejecutar la función principal
if __name__ == "__main__":
    main()
