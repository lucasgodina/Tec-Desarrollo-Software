# Se ingresa el año en curso
anio_actual = int(input("Ingrese el año actual: "))

# Se ingresa el nombre y el año de nacimiento de tres personas
personas = {}

for i in range(3):
    nombre = input("Ingrese el nombre de la persona")
    anio_nacimiento = int(input("Ingrese el año de nacimiento: "))

    personas.update({nombre: anio_nacimiento})

print(personas)
