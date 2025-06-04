"""
Imagina que trabajas en una empresa internacional con equipos distribuidos en diferentes países. Cada equipo tiene una lista de empleados, representados como diccionarios, con información sobre el nombre, la edad y el rendimiento en proyectos recientes.
Tu tarea es organizar una lista consolidada de todos los empleados de la empresa. La organización debe seguir ciertas reglas:
1. Los empleados se deben ordenar por el rendimiento en proyectos recientes de forma descendente.
2. Para aquellos con el mismo rendimiento, se deben ordenar por edad de forma ascendente. Además, deseas agrupar a los empleados por país para un análisis más efectivo. Utiliza funciones lambda.

Entrada:
- Registro de empleados (json, dic, etc)

Salida:
- Empleados agrupados.
"""

empleados = [
    {"nombre": "Lucas", "edad": 30, "rendimiento": 85, "pais": "Argentina"},
    {"nombre": "Maria", "edad": 27, "rendimiento": 95, "pais": "Argentina"},
    {"nombre": "Ana", "edad": 32, "rendimiento": 80, "pais": "Chile"},
    {"nombre": "Carlos", "edad": 29, "rendimiento": 90, "pais": "Chile"},
    {"nombre": "Pedro", "edad": 25, "rendimiento": 90, "pais": "Mexico"},
    {"nombre": "James", "edad": 35, "rendimiento": 85, "pais": "USA"},
    {"nombre": "David", "edad": 28, "rendimiento": 95, "pais": "Canada"},
    {"nombre": "Isabela", "edad": 22, "rendimiento": 80, "pais": "Mexico"},
]

from collections import defaultdict

# Agrupar empleados por país
empleados_por_pais = defaultdict(list)
for empleado in empleados:
    empleados_por_pais[empleado["pais"]].append(empleado)

# Ordenar empleados por rendimiento y edad
for pais, empleados in empleados_por_pais.items():
    empleados.sort(key=lambda x: (-x["rendimiento"], x["edad"]))

# Mostrar empleados agrupados y ordenados
for pais, empleados in empleados_por_pais.items():
    print(f"Empleados en {pais}:")
    for empleado in empleados:
        print(
            f"  Nombre: {empleado['nombre']}, Edad: {empleado['edad']}, Rendimiento: {empleado['rendimiento']}"
        )
    print()  # Línea en blanco para separar países
