# Escribir un programa que le diga al usuario que ingrese una cadena.
# El programa tiene que evaluar la cadena y decir cuantas letras mayusculas tiene.


def cuantas_mayusculas(palabra):
    mayusculas = 0
    for i in range(len(palabra)):
        if palabra[i].isupper():
            mayusculas += 1
    return mayusculas
