def es_palindromo(palabra):
    inversa = palabra[::-1]
    if palabra == inversa:
        return True
    else:
        return False


print(es_palindromo("menem"))
print(es_palindromo("neuquen"))
print(es_palindromo("lucas"))
