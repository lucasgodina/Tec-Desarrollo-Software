def superposicion(lista1, lista2):
    for i in lista1:
        for j in lista2:
            if (lista1[i] == lista2[j]):
                return True

    return False
