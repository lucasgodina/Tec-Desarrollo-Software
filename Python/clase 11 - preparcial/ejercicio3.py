# Escribir una función filtrar_palabras() que tome una lista de palabras y un
# entero n, y devuelva las palabras que tengan mas de n caracteres.


def filtrar_palabras(palabras, n):
    palabras_filtradas = []

    for palabra in palabras:
        if len(palabra) > n:
            palabras_filtradas.append(palabra)

    return palabras_filtradas


filtrar_palabras(["hola", "mundo", "python"], 5)
