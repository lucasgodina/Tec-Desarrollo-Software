personas = {}
flag = True

while flag:
    print("1. Agregar")
    print("2. Mostrar el mas chico")
    print("3. Mostrar el mas grande")
    print("4. Salir")
    opcion = input(">>> ")

    if opcion == "1":
        nombre = input("Ingrese el nombre de la persona a agregar: ")
        edad = input("Ingrese la edad de la persona a agregar: ")
        if nombre == "":
            print("El nombre no puede estar vacio")
        elif edad == "" or edad.isdecimal() == False:
            print("La edad debe ser un numero entero")
        elif int(edad) < 0:
            print("La edad no puede ser negativa")
        elif nombre in personas:
            print("La persona ya existe")
        else:
            personas.update({nombre: int(edad)})
    elif opcion == "2":
        # Opcion corta
        # print("La persona mas chica es " + min(personas, key=personas.get))

        # Opcion sin funcion min
        menor_edad = personas.get(list(personas.keys())[0])
        nombre_menor = list(personas.keys())[0]
        for persona in personas:
            print(nombre_menor)
            if personas[persona] < menor_edad:
                menor_edad = personas[persona]
                nombre_menor = persona
        print("La persona mas chica es " + nombre_menor)
    elif opcion == "3":
        # Opcion corta
        # print("La persona mas grande es " + max(personas, key=personas.get))

        # Opcion sin funcion max
        mayor_edad = personas.get(list(personas.keys())[0])
        nombre_mayor = list(personas.keys())[0]
        for persona in personas:
            if personas[persona] > mayor_edad:
                mayor_edad = personas[persona]
                nombre_mayor = persona
        print("La persona mas grande es " + nombre_mayor)
    elif opcion == "4":
        flag = False
    else:
        print("La opcion ingresada no es valida")
