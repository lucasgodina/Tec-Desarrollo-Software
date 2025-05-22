"""
Supongamos que estás construyendo un sistema de gestión de empleados
para una empresa. Crea un sistema de clases que maneje la información de
los empleados, incluyendo empleados a tiempo completo y empleados a
tiempo parcial.
- Clase base: `Empleado`
- Atributos: nombre, apellido, salario base
- Clase derivada: `EmpleadoTiempoCompleto` (hereda de `Empleado`)
- Atributo adicional: bono anual
- Clase derivada: `EmpleadoTiempoParcial` (hereda de `Empleado`)
- Atributo adicional: horas trabajadas por semana

Resuelve el problema creando instancias de estas clases y calculando los
salarios totales para diferentes tipos de empleados.
"""

import Empleado, EmpleadoTiempoCompleto, EmpleadoTiempoParcial


def main():
    # Crear instancias de empleados
    empleado1 = Empleado.Empleado("Juan", "Pérez", 3000)
    empleado2 = EmpleadoTiempoCompleto.EmpleadoTiempoCompleto(
        "María", "López", 4000, 500
    )
    empleado3 = EmpleadoTiempoParcial.EmpleadoTiempoParcial(
        "Carlos", "García", 2000, 20
    )

    # Calcular salarios totales
    salario_empleado1 = empleado1.calcular_salario_total()
    salario_empleado2 = empleado2.calcular_salario_total()
    salario_empleado3 = empleado3.calcular_salario_total()

    # Imprimir resultados
    print(
        f"Salario total de {empleado1.nombre} {empleado1.apellido}: {salario_empleado1}"
    )
    print(
        f"Salario total de {empleado2.nombre} {empleado2.apellido}: {salario_empleado2}"
    )
    print(
        f"Salario total de {empleado3.nombre} {empleado3.apellido}: {salario_empleado3}"
    )


if __name__ == "__main__":
    main()
