try:
    numero = int(input("Introduce un número: "))
    print(f"Has introducido el número: {numero}")
except ValueError:
    print("Error: No has introducido un número válido.")
