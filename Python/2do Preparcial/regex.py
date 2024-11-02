import re

# Ejemplo 1: Coincidencia simple
# Este ejemplo busca la palabra "hola" en el texto.
texto = "hola mundo"
patron = r"hola"
coincidencia = re.search(patron, texto)
if coincidencia:
    print("Se encontró:", coincidencia.group())
else:
    print("No se encontró ninguna coincidencia")

# Ejemplo 2: Coincidencia con caracteres especiales
# Este ejemplo busca cualquier dígito en el texto.
texto = "Mi número es 12345"
patron = r"\d+"
coincidencia = re.search(patron, texto)
if coincidencia:
    print("Se encontró un número:", coincidencia.group())
else:
    print("No se encontró ningún número")

# Ejemplo 3: Coincidencia con múltiples patrones
# Este ejemplo busca palabras que comiencen con "h" y terminen con "o".
texto = "hola mundo, halo, hero"
patron = r"h\w+o"
coincidencias = re.findall(patron, texto)
print("Palabras que coinciden:", coincidencias)

# Ejemplo 4: Reemplazo de texto
# Este ejemplo reemplaza todas las ocurrencias de "mundo" con "amigo".
texto = "hola mundo, adiós mundo"
patron = r"mundo"
nuevo_texto = re.sub(patron, "amigo", texto)
print("Texto modificado:", nuevo_texto)

# Ejemplo 5: División de texto
# Este ejemplo divide el texto en una lista de palabras usando espacios como delimitador.
texto = "hola mundo, cómo estás?"
patron = r"\s+"
palabras = re.split(patron, texto)
print("Palabras:", palabras)

# Ejemplo 6: Uso de grupos
# Este ejemplo captura el nombre y el dominio de una dirección de correo electrónico.
texto = "mi correo es ejemplo@dominio.com"
patron = r"(\w+)@(\w+\.\w+)"
coincidencia = re.search(patron, texto)
if coincidencia:
    print("Nombre de usuario:", coincidencia.group(1))
    print("Dominio:", coincidencia.group(2))
else:
    print("No se encontró ninguna dirección de correo electrónico")
