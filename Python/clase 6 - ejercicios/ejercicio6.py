def inversa(palabra):
    palabra_inversa = ""

    for char in palabra:
        palabra_inversa.join(char, palabra_inversa)
    return palabra_inversa


print(inversa("pepe"))
