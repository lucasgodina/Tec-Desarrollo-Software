import re

<<<<<<< HEAD
# Ejemplo 1: Coincidir una palabra específica
pattern = r"hola"
text = "hola mundo"
match = re.search(pattern, text)
if match:
    print("Se encontró 'hola' en el texto")

# Ejemplo 2: Coincidir un número de teléfono (formato: 123-456-7890)
pattern = r"\d{3}-\d{3}-\d{4}"
text = "Mi número es 123-456-7890"
match = re.search(pattern, text)
if match:
    print("Se encontró un número de teléfono")

# Ejemplo 3: Coincidir una dirección de correo electrónico
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
text = "Mi correo es ejemplo@dominio.com"
match = re.search(pattern, text)
if match:
    print("Se encontró una dirección de correo electrónico")

# Ejemplo 4: Coincidir todas las palabras que comienzan con una letra mayúscula
pattern = r"\b[A-Z][a-z]*\b"
text = "Hola Mundo, esto es una Prueba"
matches = re.findall(pattern, text)
print("Palabras que comienzan con mayúscula:", matches)

# Ejemplo 5: Reemplazar todas las apariciones de una palabra por otra
pattern = r"mundo"
replacement = "tierra"
text = "hola mundo"
new_text = re.sub(pattern, replacement, text)
print("Texto modificado:", new_text)
=======
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
>>>>>>> 4a23642f34a0ab7df19d93af58be603e9bb86e08
