alumnos = []
flag = True

while (flag):
    print("Ingrese el numero de la operacion que desea ejecutar:")
    print("1 - Ver la lista de alumnos")
    print("2 - Añadir un alumno a la lista")
    print("3 - Salir")
    opcion = input(">>> ")
    if opcion == "1":
        print("Lista de alumnos:")
        for alumno in alumnos:
            print(alumno[0] + " - " + alumno[1] + " cursos.")
    elif opcion == "2":
        nombre = input("Ingrese el nombre del alumno: ")
        cursos = input("Ingrese la cantidad de cursos: ")
        alumnos.append([nombre, cursos])
        print("¡El alumno fue añadido a la lista!")
    elif opcion == "3":
        print("¡Gracias por utilizar el programa!")
        flag = False
    else:
        print("Ingrese una opcion valida")
