edad = int(input("Ingrese su edad: "))
ingresos = int(input("Ingrese su ingreso mensual: "))

if edad >= 18 and ingresos >= 10000:
    print("Usted debe tributar")
else:
    print("Usted NO debe tributar")
