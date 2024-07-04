def mas_larga(palabras):
    palabra_mas_larga = ""
    for palabra in palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    return palabra_mas_larga


palabras = ["Lucas", "Jazmin", "Jorgelina", "Nadia", "Camila"]
print(mas_larga(palabras))
