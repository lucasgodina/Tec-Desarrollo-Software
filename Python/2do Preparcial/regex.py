import re

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
