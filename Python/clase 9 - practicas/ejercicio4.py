numeros_ganadores = []

for i in range(10):
    numero = int(input("Ingrese el numero ganador: "))
    numeros_ganadores.append(numero)

numeros_ganadores.sort()

print(numeros_ganadores)
