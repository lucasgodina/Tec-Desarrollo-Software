def soloNumeros():
    a = input("Ingrese el numero: ")
    while a.isdecimal() == False:
        a = input("Ingrese un numero valido: ")
    print(a + " es un numero")

soloNumeros()
