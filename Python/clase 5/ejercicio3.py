# Escribir un programa que pregunte el
# nombre del usuario en la consola y después
# de que el usuario lo introduzca muestre por
# pantalla tiene letras, donde es el nombre
# de usuario en mayúsculas y es el número de
# letras que tienen el nombre.
nombre = input("Ingrese su nombre: ")

print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")
