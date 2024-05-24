contraseña = "python"
adivina = input("Ingrese su contraseña: ")
adivina.lower()
if adivina == contraseña:
    print("Adivinaste!")
    flag = False
else:
    print("Perdiste!")
