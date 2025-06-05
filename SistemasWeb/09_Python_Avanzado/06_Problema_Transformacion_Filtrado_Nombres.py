"""
Imagina que te encuentras desarrollando una herramienta de procesamiento de nombres para una aplicación de gestión de contactos.
Tienes una lista de nombres en el formato "Apellido, Nombre", realiza las siguientes tareas:
1. Utiliza la función lambda para transfromar una lista de nombres completos al nuevo formato.
2. Filtra la lista para incluir solo los nombres que contienen al menos dos vocales y tienen una longitud mayor a 10 caracteres.

Entrada:
- Lista de nombres, ej, ["Perez, Juan", "Lopez, Maria", "Gomez, Ana"]

Salida:
- Lista de nombres transformados y filtrados, ej: ["Juan Perez", "Maria Lopez", "Ana Gomez"]
"""


def transformar_nombres(nombres):
    """
    Transforma una lista de nombres.
    Convierte nombres del formato "Apellido, Nombre" a "Nombre Apellido".
    """
    return list(map(lambda n: f"{n.split(', ')[1]} {n.split(', ')[0]}", nombres))


def filtrar_nombres(nombres):
    """
    Filtra una lista de nombres.
    Retorna solo aquellos nombres que contienen al menos dos vocales y tienen una longitud mayor a 10 caracteres.
    """
    return list(
        filter(
            lambda n: sum(1 for c in n if c.lower() in "aeiou") >= 2 and len(n) > 10,
            nombres,
        )
    )


# Ejemplo de uso
if __name__ == "__main__":
    # Lista de nombres
    nombres = [
        "Perez, Juan",
        "Lopez, Maria",
        "Gomez, Ana",
        "Fernandez, Carlos",
        "Martinez, Isabella",
    ]

    # Transformar nombres
    nombres_transformados = transformar_nombres(nombres)

    # Filtrar nombres
    nombres_filtrados = filtrar_nombres(nombres_transformados)

    print("Nombres transformados y filtrados:", nombres_filtrados)
