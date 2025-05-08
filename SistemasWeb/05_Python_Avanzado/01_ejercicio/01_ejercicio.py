"""
Un problema común al solicitar una entrada numérica ocurre cuando las personas ingresan texto en lugar de números. Cuando intentas convertir la entrada a un entero (int), obtendrás un ValueError. Escribe un programa que solicite dos números. Suma los números y muestra el resultado. Captura el ValueError si alguno de los valores de entrada no es un número e imprime un mensaje de error amigable. Prueba tu programa ingresando dos números y luego ingresando texto en lugar de un número. Envuelve tu código del en un bucle while para que el usuario pueda continuar ingresando números incluso si comete un error ingresando texto en lugar de un número.
"""

while True:
    try:
        # Solicitar dos números al usuario
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))

        # Sumar los números
        resultado = num1 + num2

        # Mostrar el resultado
        print(f"La suma de {num1} y {num2} es: {resultado}")

    except ValueError:
        print("Error: Por favor, ingrese un número válido.")

    # Preguntar si desea continuar
    continuar = input("¿Desea ingresar otros números? (s/n): ")
    if continuar.lower() != "s":
        break
