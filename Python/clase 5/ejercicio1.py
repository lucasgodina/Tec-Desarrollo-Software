# Escribir un programa que pregunte el nombre del usuario en la
# consola y un número entero e imprima por pantalla en líneas distintas
# el nombre del usuario tantas veces como el número introducido.
nombre = input("Ingrese el nombre del usuario: ")
cantidad = input("Ingrese cuantas veces quiere repetirlo: ")
i = 0

# Version con while
while i < int(cantidad):
    print(nombre)
    i += 1

# Version con for
# for i in range(cantidad):
#    print(nombre)
