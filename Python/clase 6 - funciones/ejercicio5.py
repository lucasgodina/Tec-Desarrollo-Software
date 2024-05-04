# personas = []

personas = {}


def menu():
    funciona = True
    while (funciona):
        print("1.Agregar")
        print("2.Mostrar el mas chico")
        print("3.Mostrar el mas grande")
        print("4.Salir")
        opcion = input("Ingrese la opcion seleccionada: ")
        if (opcion == "1"):
            agregar()
        elif (opcion == "2"):
            print("La persona mas chica es " + buscar_mas_chico())
        elif (opcion == "3"):
            print("La persona mas grande es " + buscar_mas_grande())
        elif (opcion == "4"):
            funciona = False
        else:
            print("La opcion ingresada no es valida")


def agregar():
    nombre = input("Ingrese el nombre de la persona a agregar: ")
    edad = int(input("Ingrese la edad de la persona a agregar: "))
    personas[nombre] = edad
    print(nombre + " fue ingresado a la lista.")


def buscar_mas_chico():
    nombre = list(personas.keys())[0]
    menorEdad = list(personas.values())[0]
    for persona in personas:
        if personas[persona] < menorEdad:
            nombre = persona
            menorEdad = personas[persona]
    return nombre


def buscar_mas_grande():
    nombre = list(personas.keys())[0]
    menorEdad = list(personas.values())[0]
    for persona in personas:
        if personas[persona] < menorEdad:
            nombre = persona
            menorEdad = personas[persona]
    return nombre


menu()
