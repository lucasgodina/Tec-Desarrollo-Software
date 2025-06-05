"""
Imagina que eres parte de una empresa de comercio electrónico y tienes información detallada sobre las ventas de productos.
Cada venta se representa como un diccionario, que incluye el nombre del producto, la fecha de venta, el monto de la venta y la ubicación del comprador.
Realizar un análisis avanzado de estas ventas.
1. Filtra las ventas realizadas en el último trimestre del año.
2. Selecciona solo las ventas de productos con un monto superior a $500.
3. Agrupa las ventas por ubicación del comprador.
4. Calcula el promedio del monto de venta para cada ubicación.
5. Ordena las ubicaciones por el promedio del monto de venta de forma descendente.
Utilizar funciones lambda.

Entrada:
- Registro de ventas

Salida:
- Ubicaciones por promedio, ej: [Chile, Ecuador]
"""

import datetime
from collections import defaultdict


# Función para analizar las ventas
def analizar_ventas(ventas):
    # 1. Filtra las ventas realizadas en el último trimestre del año.
    ventas_trimestre = list(
        filter(lambda v: int(v["fecha"].split("-")[1]) in [10, 11, 12], ventas)
    )

    # 2. Selecciona solo las ventas de productos con un monto superior a $500.
    ventas_filtradas = list(filter(lambda v: v["monto"] > 500, ventas_trimestre))

    # 3. Agrupa las ventas por ubicación del comprador.
    ventas_por_ubicacion = defaultdict(list)
    list(
        map(lambda v: ventas_por_ubicacion[v["ubicacion"]].append(v), ventas_filtradas)
    )

    # 4. Calcula el promedio del monto de venta para cada ubicación.
    promedios_ubicacion = {}
    for ubicacion, ventas in ventas_por_ubicacion.items():
        promedio = sum(v["monto"] for v in ventas) / len(ventas)
        promedios_ubicacion[ubicacion] = promedio

    # 5. Ordena las ubicaciones por el promedio del monto de venta de forma descendente.
    ubicaciones_ordenadas = sorted(
        promedios_ubicacion.items(), key=lambda x: x[1], reverse=True
    )

    return ubicaciones_ordenadas


# Ejemplo de uso
if __name__ == "__main__":

    # Registro de ventas
    ventas = [
        {
            "producto": "Laptop",
            "fecha": "2023-10-15",
            "monto": 1200,
            "ubicacion": "Chile",
        },
        {
            "producto": "Smartphone",
            "fecha": "2023-11-05",
            "monto": 800,
            "ubicacion": "Ecuador",
        },
        {
            "producto": "Tablet",
            "fecha": "2023-09-20",
            "monto": 300,
            "ubicacion": "Chile",
        },
        {
            "producto": "Monitor",
            "fecha": "2023-12-01",
            "monto": 600,
            "ubicacion": "Perú",
        },
        {
            "producto": "Teclado",
            "fecha": "2023-10-10",
            "monto": 150,
            "ubicacion": "Ecuador",
        },
        {
            "producto": "Mouse",
            "fecha": "2023-11-15",
            "monto": 200,
            "ubicacion": "Argentina",
        },
        {
            "producto": "Auriculares",
            "fecha": "2023-12-20",
            "monto": 700,
            "ubicacion": "Argentina",
        },
    ]
    ubicaciones_ordenadas = analizar_ventas(ventas)
    print("Ubicaciones ordenadas por promedio del monto de venta:")
    for ubicacion, promedio in ubicaciones_ordenadas:
        print(f"{ubicacion}: ${promedio:.2f}")
